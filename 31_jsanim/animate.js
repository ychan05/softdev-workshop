var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var  stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID;

var clear = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 100;
var growing = true;

var drawDot = () =>{
    clear();
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
}

var stopIt = () => {
    console.log("stopit invoked...");
    window.cancelAnimationFrame(requestID);
    console.log("requestID cancelled");

}


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);