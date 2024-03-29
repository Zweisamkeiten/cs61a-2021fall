(define (vir-fib n)
         (cond
             ((= n 0) 0)
             ((= n 1) 1)
             (else (+ n (vir-fib (- n 1))))
             )
         )
     
(vir-fib 0)
(vir-fib 1)
(vir-fib 10)

(define with-list
    (list
        (list 'a 'b)
        'c 'd (list 'e)
    )
)
(draw with-list)

(define with-quote
    '(
        (a b)
        c d (e)
    )

)
(draw with-quote)

(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        helpful-list another-helpful-list
    )
)
(draw with-cons)

(define (list-concat a b)
    (cond
        ((and (null? a) (null? b)) nil)
        ((null? a) (cons (car b) (list-concat (cdr b) a)))
        (else (cons (car a) (list-concat (cdr a) b)))
        )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

(define (map-fn fn lst)
    (if (null? lst) nil
        (cons (fn (car lst)) (map-fn fn (cdr lst)))
        )
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)

(define (make-tree label branches) (cons label branches))

(define (label tree)
    (car tree)
)

(define (branches tree)
    (cdr tree)
)

(make-tree 1 (list (make-tree 2 '()) (make-tree 3 '())))
; expect (1 (2) (3))

(define (tree-sum tree)
    (+ (label tree) (sum (map tree-sum (branches tree))))
)

(define (sum lst)
    (if (null? lst) 0
        (+ (car lst) (sum (cdr lst))))
)

(define t (make-tree 1 (list (make-tree 2 '()) (make-tree 3 '()))))
(expect (tree-sum t) 6)
