(define (my-filter func lst) 
  (if (null? lst) ()
    (if (func (car lst))
      (cons (car lst) (my-filter func (cdr lst)))
      (my-filter func (cdr lst))
    )
  )
)

(define (interleave s1 s2)
  (cond 
    ((and (null? s1) (null? s2)) ())
    ((null? s1) (cons (car s2) (interleave (cdr s2) s1)))
    ((null? s2) (cons (car s1) (interleave (cdr s1) s2)))
    (else (cons (car s1) (interleave s2 (cdr s1))))
    )
)

(define (accumulate merger start n term)
  (if (= n 0)
    start
    (accumulate merger (merger start (term n)) (- n 1) term)
  )
)

(define (no-repeats lst)
  (if (null? lst) ()
    (cons (car lst)
          (no-repeats 
            (my-filter (lambda (x) (not (= (car lst) x)))
               lst)
          )
    )
  )
)
