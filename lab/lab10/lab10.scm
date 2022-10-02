(define (over-or-under num1 num2) (cond
                                      ((< num1 num2) -1)
                                      ((> num1 num2) 1)
                                      (else 0)))

(define (make-adder num) (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define lst '((1) 2 (3 4) 5))

(define (remove item lst) 
    (if (null? lst) nil
        (if (= (car lst) item)
            (remove item (cdr lst))
            (cons (car lst) (remove item (cdr lst))))))