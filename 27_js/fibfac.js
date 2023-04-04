// Team Infinite Synergy :: Yat Long Chan, David Deng 
// SoftDev pd8
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// Time spent: 0.5 hours
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact(n) {
    if (n < 2) {
        return 1;
    }
    return n * fact(n - 1);
}
console.log(fact(1))
console.log(fact(2))
console.log(fact(3))
console.log(fact(4))
console.log(fact(5))


function fib(n) {
    if (n == 0 || n == 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}
console.log(fib(0))
console.log(fib(1))
console.log(fib(2))
console.log(fib(3))
console.log(fib(4))
