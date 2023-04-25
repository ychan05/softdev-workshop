/*
Infinite Synergy: Yat Long Chan, David Deng
SoftDev pd8
K30 -- basic canvas work in JS
2023-04-25t
time spent: 
*/

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

// set shape color
ctx.fillStyle = "red";
ctx.strokeStyle = "red";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
};

var drawRect = (e) => {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 80, 100);
};

var drawCircle = (e) => {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fill();
};

var draw = (e) => {
    if (mode === "rect") {
        drawRect(e);
    } else {
        drawCircle(e);
    }
};

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
};

c.addEventListener("click", draw); //passes the mouse event as parameter for the function

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
