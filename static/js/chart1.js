// 전력 예측 그래프 코드

const getMeasurementData = async () => {
    const response = await fetch("/test");
    const jsonData = await response.json();
    const { test1 } = jsonData;
    const tmp = [NaN, NaN, NaN];
    const test1Array = test1.concat(tmp);
    console.log(test1Array);
    return test1Array;
};

const getForecastData = async () => {
    const response = await fetch("/test");
    const jsonData = await response.json();
    const { test2 } = jsonData;
    const tmp = [NaN, NaN, NaN, NaN, NaN];
    const test2Array = tmp.concat(test2);
    console.log(test2Array);
    return test2Array;
};

(async () => {
    const labels = ["1", "2", "3", "4", "5", "6", "7", "9"];
    const data = {
        labels: labels,
        datasets: [
            {
                label: "측정치",
                data: await getMeasurementData(),
                fill: false,
                borderColor: "#45e8bc",
                tension: 0.1,
            },
            {
                label: "예상치",
                data: await getForecastData(),
                fill: false,
                borderColor: "rgb(0,100,0)",
                tension: 0.1,
            },
        ],
    };
    // </block:setup>

    // <block:config:0>
    const config = {
        type: "line",
        data: data,
    };
    // </block:config>

    const ctx = document.getElementById("lineChart").getContext("2d");
    const myChart = new Chart(ctx, config);
})();
