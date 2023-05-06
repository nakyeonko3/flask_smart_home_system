(async () => {
    const labels = ["1", "2", "3", "4", "5", "6", "7", "9"];
    const data = {
        labels: labels,
        datasets: [
            {
                label: "측정치",
                data: [65, 59, 80, 81, 80, 80, 81, 80],
                fill: false,
                borderColor: "red",
                // segment: {
                //     borderColor: (ctx) =>
                //         ctx.p0.parsed.x >= 4 ? "blue" : "red",
                // },
                tension: 0.1,
            },
            {
                label: "이상치",
                data: [65, 11, 78, 81, 80, 46, 25, 30],
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

    const ctx = document.getElementById("doughnut").getContext("2d");
    const myChart = new Chart(ctx, config);
})();
