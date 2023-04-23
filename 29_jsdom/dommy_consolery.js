// Team Phantom Tollbooth :: Yat Long Chan, Jacob Guo
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-24m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function (x) {
    var j = 30;
    return j + x;
};


//instantiate an object
var o = {
    'name': 'Thluffy',
    age: 1024,
    items: [10, 20, 30, 40],
    morestuff: { a: 1, b: 'ayo' },
    func: function (x) {
        return x + 30;
    }
};

//adds a new item to the list
var addItem = function (text) {
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//remove an item from the list with index n
var removeItem = function (n) {
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//adds red class to all the list items
var red = function () {
    var items = document.getElementsByTagName("li");
    for (var i = 0; i < items.length; i++) {
        items[i].classList.add('red');
    }
};

//makes even numbered items in list get red class and odd ones blue
var stripe = function () {
    var items = document.getElementsByTagName("li");
    for (var i = 0; i < items.length; i++) {
        if (i % 2 == 0) {
            items[i].classList.add('red');
        } else {
            items[i].classList.add('blue');
        }
    }
};

//insert your implementations here for...
// FIB
function fact(n) {
    if (n < 2) return 1;
    return n * fact(n - 1);
}

// FAC
function fib(n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}

// GCD
function GCD(a, b) {
    if (b === 0) return a;
    return GCD(b, a % b);
}

const fibBtn = document.getElementsByClassName('fib')[0];
fibBtn.addEventListener('click', () => {
    const fibTxt = document.getElementsByClassName('fib-text')[0];
    let n = Math.round(30 * Math.random())
    //   console.log(fib(10));
    //   fibTxt.innerHTML = "fib(" + n + ") = " + fib(n);
    fibTxt.innerHTML = `fib(${n}) = ${fib(n)}`
})

const factBtn = document.getElementsByClassName('fact')[0];
factBtn.addEventListener('click', () => {
    const factTxt = document.getElementsByClassName('fact-text')[0];
    let n = Math.round(30 * Math.random())
    factTxt.innerHTML = `fact(${n}) = ${fact(n)}`
})

const gcdBtn = document.getElementsByClassName('gcd')[0];
gcdBtn.addEventListener('click', () => {
    const gcdTxt = document.getElementsByClassName('gcd-text')[0];
    let n = Math.round(30 * Math.random())
    let m = Math.round(100 * Math.random())

    gcdTxt.innerHTML = `GCD(${n}, ${m}) = ${GCD(n, m)}`
})

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};