/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Infinite Synergy:: Yat Long Chan, David Deng
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-20r
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text; //set text of element
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
var fibonacci = document.getElementById('fib');

var fib = function(i) {
  if (i < 2) {return i;}
  else {
    return fib(i - 1) + fib(i - 2);
  }
}

fibonacci.addEventListener('click', () => {
  document.getElementById('fib-txt').innerHTML = "fib(5) = " + fib(5);
}); 

// FAC
var factorial = document.getElementById('fac');

var fac = function(i) {
  if (i === 1) {
    return 1;
  }
  while (i > 1) {
    return i * fac(i - 1);
  }
}

factorial.addEventListener('click', () => {
  document.getElementById('fac-txt').innerHTML = "fac(5) = " + fac(5);
});

// GCD
var GCD = document.getElementById('gcd');

var gcd = function(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

GCD.addEventListener('click', () => {
  document.getElementById('gcd-txt').innerHTML = "gcd(25, 10) = " + gcd(25, 10);
});

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

