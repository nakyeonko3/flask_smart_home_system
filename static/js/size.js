const maxWith1115 = () => {
    const sidebar = document.querySelector(".sidebar");
    const main = document.querySelector(".main");
    const cards = document.querySelector(".cards");
    const charts = document.querySelector(".charts");
    const topbar = document.querySelector(".topbar");

    if (window.innerWidth < 1115 && window.innerWidth > 880) {
        sidebar.style.width = "60px";
        main.style.left = "60px";
        main.style.width = "calc(100% - 60px)";
    } else if (window.matchMedia("(max-width: 880px)").matches) {
        cards.style.gridTemplateColumns = "repeat(2, 1fr)";
        charts.style.gridTemplateColumns = "1fr";
    } else if (window.matchMedia("(max-width: 500px)").matches) {
        topbar.style.gridTemplateColumns = "1fr 5fr 0 0.4fr 1fr";
        cards.style.gridTemplateColumns = "1fr";
    } else {
        sidebar.style.width = "260px";
    }
};

const handleResizeEvenet = () => {
    maxWith1115();
};

maxWith1115();

window.addEventListener("resize", handleResizeEvenet);
