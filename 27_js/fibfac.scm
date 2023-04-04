#lang scheme
;Team Infinite Synergy :: Yat Long Chan, David Deng
;SoftDev pd0
;K27 -- Basic functions in JavaScript
;2023-04-04t

;Scheme Antecedents for JS work

;factorial:
(define
  fact (lambda (n)
  (if (< n 2)
      1
      (* n (fact(- n 1))
  ))))

(fact 1) ;"...should be  1"
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;fib:
(define
  fib (lambda (n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib(- n 1)) (fib(- n 2)))
  ))))

(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"
;=================================================================

