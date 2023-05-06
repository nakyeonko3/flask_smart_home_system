const data = [
    { x: "Jan", net: 100, cogs: 50, gm: 50 },
    { x: "Feb", net: 120, cogs: 55, gm: 75 },
];
const cfg = {
    type: "bar",
    data: {
        labels: ["Jan", "Feb"],
        datasets: [
            {
                label: "Net sales",
                data: data,
                parsing: {
                    yAxisKey: "net",
                },
            },
            {
                label: "Cost of goods sold",
                data: data,
                parsing: {
                    yAxisKey: "cogs",
                },
            },
            {
                label: "Gross margin",
                data: data,
                parsing: {
                    yAxisKey: "gm",
                },
            },
        ],
    },
};

const ctx = document.getElementById("lineChart").getContext("2d");
const myChart = new Chart(ctx, cfg);
