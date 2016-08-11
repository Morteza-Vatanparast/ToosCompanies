var duration = 0;
var delay = 0;

function drawClock(drawPlace, timestamp) {
    var canvas = document.getElementById(drawPlace),
        context = canvas.getContext("2d"),
        centerX = canvas.width / 2,
        centerY = canvas.height / 2,
        radius = canvas.width / 2 - 20;

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.lineCap = "round";
    context.beginPath();
    context.arc(centerX, centerY, radius - 10, 0, 2 * Math.PI, false);
    context.fillStyle = '#ccc';
    context.fill();
    context.closePath();
    context.restore();

    context.beginPath();
    context.arc(centerX, centerY, radius - 14, 0, 2 * Math.PI, false);
    context.fillStyle = '#fff';
    context.fill();
    context.closePath();
    context.restore();

    // Center Circle
    context.beginPath();
    context.arc(centerX, centerY, 4, 0, 2 * Math.PI, false);
    context.lineWidth = 3;
    context.strokeStyle = '#555';
    context.stroke();
    context.closePath();
    context.restore();

    context.translate(centerX, centerY);

    context.fillStyle = '#555';
    context.font = radius * 0.18 + "px SDF";
    context.textBaseline = "middle";
    context.textAlign = "center";
    for (num = 0; num < 12; num++) {
        ang = (num + 1) * Math.PI / 6;
        context.rotate(ang);
        context.translate(0, -radius * 0.60);
        context.rotate(-ang);
        context.fillText((num+1).toString(), 0, 0);
        context.rotate(ang);
        context.translate(0, radius * 0.60);
        context.rotate(-ang);
    }

    for (var i = 1; i <= 60; i++) {
        angle = Math.PI / 30 * i;
        sineAngle = Math.sin(angle);
        cosAngle = -Math.cos(angle);

        if (i % 5 == 0) {
            context.lineWidth = 2;
            iPointX = sineAngle * (radius - 25);
            iPointY = cosAngle * (radius - 25);
            oPointX = sineAngle * (radius - 20);
            oPointY = cosAngle * (radius - 20);
        } else {
            context.lineWidth = 0.8;
            iPointX = sineAngle * (radius - 22);
            iPointY = cosAngle * (radius - 22);
            oPointX = sineAngle * (radius - 20);
            oPointY = cosAngle * (radius - 20);
        }

        context.beginPath();
        context.moveTo(iPointX, iPointY);
        context.lineTo(oPointX, oPointY);
        context.stroke();
    }

    var now = timestamp,

        hrs = now.getHours(),
        min = now.getMinutes(),
        sec = now.getSeconds();

    // Set Hands Variables
    var sangle = (Math.PI / 30 * sec),
        sPointX = Math.sin(sangle) * (radius - 50),
        sPointY = -Math.cos(sangle) * (radius - 50);

    // Draw seconds hand
    context.beginPath();
    context.lineWidth = 2;
    context.moveTo(0, 0);
    context.strokeStyle = "#f00";
    context.lineTo(sPointX, sPointY);
    context.stroke();
    context.closePath();

    // Draw minutes hand
    context.beginPath();
    context.lineWidth = 4;
    context.strokeStyle = "#555555";
    sangle = (Math.PI / 30 * (min + (sec / 60)));
    sPointX = Math.sin(sangle) * (radius - 48);
    sPointY = -Math.cos(sangle) * (radius - 48);
    context.moveTo(0, 0);
    context.lineTo(sPointX, sPointY);
    context.stroke();
    context.closePath();

    // Draw hours hand
    context.beginPath();
    context.lineWidth = 6;
    context.strokeStyle = "#555555";
    sangle = (Math.PI / 6 * (hrs + (min / 65) + (sec / 3600)));
    sPointX = Math.sin(sangle) * (radius - 65);
    sPointY = -Math.cos(sangle) * (radius - 65);
    context.moveTo(0, 0);
    context.lineTo(sPointX, sPointY);
    context.stroke();
    context.closePath();

    context.restore();
    context.translate(-centerX, -centerY);
}

setInterval(function () {
    $("#canvasClock").css("visibility", 'visible');
    var d = new Date(year, month, day, hour, minute, second, 0);
    d.setSeconds(d.getSeconds() + duration + delay);

    drawClock('analogClock', d);

    duration = duration + 1;

    var hh = d.getHours();
    var m = d.getMinutes();
    var s = d.getSeconds();

    var dd = "ق.ظ";
    var h = hh;

    if (h >= 12) {
        h = hh - 12;
        dd = "ب.ظ";
    }

    if (h == 0) {
        h = 12;
    }

    m = m < 10 ? "0" + m : m;
    s = s < 10 ? "0" + s : s;
    h = h < 10 ? "0" + h : h;

    document.getElementById('digitalClock').innerHTML = (h + ':' + m + ':' + s + ' ' + '<strong>' + dd + '</strong>');
}, 1000);