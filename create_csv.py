import pandas as pd
from datetime import datetime


def append_csvfile(sensor_value, file_name="sensor.csv"):
    # Create a new row with current datetime and sensor value
    new_row = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Sensor": sensor_value,
    }

    # Append the new row to the existing csv file
    with open(file_name, "a") as f:
        writer = pd.DataFrame([new_row])
        writer.to_csv(f, header=f.tell() == 0, index=False, lineterminator="\n")
