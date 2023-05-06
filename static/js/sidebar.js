const sidebar = document.querySelector(".sidebar");
const dashboard = sidebar.querySelector("#dashboard");
const odd = sidebar.querySelector("#odd");
const mypage = sidebar.querySelector("#mypage");
const help = sidebar.querySelector("#help");

const cards = document.querySelector(".cards");

const charts = document.querySelector(".charts");
const lineChart = charts.querySelector(".lineChart");
const doughnutChart = charts.querySelector(".doughnut-chart");
console.log(lineChart);
console.log(doughnutChart);

mypage.addEventListener("click", () => {
    for (const child of cards.children) {
        child.style.display = "none";
    }
    for (const child of charts.children) {
        child.style.display = "none";
    }
});

odd.addEventListener("click", () => {
    for (const child of cards.children) {
        child.style.display = "none";
    }
    for (const child of charts.children) {
        child.style.display = "none";
    }
    console.log("clicked");
});

console.log(mypage);

dashboard.addEventListener("click", () => {
    for (const child of cards.children) {
        child.style.display = "flex";
    }
    for (const child of charts.children) {
        child.style.display = "block";
    }
});
