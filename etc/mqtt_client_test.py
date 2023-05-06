TOPIC = "common"
HOSTNAME = "nakyeonko3.local"
import paho.mqtt.client as mqtt
import time


df = pd.DataFrame([], columns=["Date", "Sensor"])


def make_csvfile(sensor_value, file_name="sensor.csv"):
    global df
    new_line = pd.DataFrame(
        {
            "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Sensor": [sensor_value],
        }
    )
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv(file_name, index=False)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))


def make_csvfile(sensor_value):
    print("hello, world")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(HOSTNAME)  # 접속할 호스트명

client.subscribe(TOPIC, 1)
client.loop_forever()
