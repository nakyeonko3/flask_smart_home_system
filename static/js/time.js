const dateTime = document.querySelector(".date-time");

const locale = navigator.language;
const options = {
    dateStyle: "medium",
    timeStyle: "medium",
};

function setTimeNow() {
    const today = new Date();
    dateTime.innerText = new Intl.DateTimeFormat(locale, options).format(today);
}

const today = new Date();
dateTime.innerText = new Intl.DateTimeFormat(locale, options).format(today);

setInterval(() => setTimeNow(), 1000);
