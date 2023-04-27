/*
Infinite Synergy: Yat Long Chan, David Deng
SoftDev pd8
K32 -- screensaver in canvas JS
2023-04-27r
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var  stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID;

var clear = (e) => {
    e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 100;
var growing = true;

var drawDot = () =>{
    // clear();
    ctx.clearRect(0, 0, c.width, c.height);
    if(radius === c.height / 2) {growing = false}
    if(radius === 0) {growing = true}
        if (growing){
            radius++;
        }
        else{
            radius--;
        }
        console.log(radius);
        ctx.beginPath();
        ctx.arc(c.width / 2, c.height / 2, radius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.fill();
        window.cancelAnimationFrame(requestID);
        requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 90;
    var rectHeight = 60;

    var rectX = (Math.random() * (c.width - rectWidth));
    var rectY = (Math.random() * (c.height - rectHeight));

    var xVel = 2;
    var yVel = 2;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

        if (rectX + rectWidth >= c.width || rectX  <= 0) {
            xVel = -xVel;
        }

        if (rectY + rectHeight >= c.height || rectY <= 0) {
            yVel = -yVel;
        }

        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};


dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);
