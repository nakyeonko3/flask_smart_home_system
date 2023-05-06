import { config } from "../static/js/chart1.js";

const ctx = document.getElementById("lineChart").getContext("2d");
const myChart = new Chart(ctx, config);
