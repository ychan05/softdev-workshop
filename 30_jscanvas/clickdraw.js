//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

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
    console.log("mouseclick registered at client", e.clientX, e.clientY);
    ctx.fillRect(mouseX, mouseY, 80, 100);
};

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, Math.PI * 2, true);
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


var clear = () => {
    ctx.clearRect(0, 0, c.width, c.height);
};

c.addEventListener("click", draw); //passes the mouse event as parameter for the function
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var bClear = document.getElementById("buttonClear");
bClear.addEventListener("click", clear);
