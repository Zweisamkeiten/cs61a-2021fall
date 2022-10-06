---
date created: 2022-10-02 15:28
date updated: 2022-10-02 15:59
---

# Scheme

## Scheme expression

**Lisp** 编程语言在1958年推出
Lisp 的 Scheme 方言 是1970年代引入，并且现今由标准委员会维护.

函数式编程

- Primitive expression: `2` `3.3` `#t` `#f` `+` `quotient` 原始表达式
- 组合 `(quotient 10 2)` `(not #t)`
- 数字是自我评估(evaluating)的 符号绑定到值
- 调用表达式是在括号中包含一个运算符和0或多个操作数

## Special forms

```lisp
(if <predicate> <consequent> <alternative>)

(and <e1> .. <en>)
(or <e1> ... <en>)

(define <symbol> <expression>)

(define (<symbol> <formal parameters>) <body>)
# 构造一个新的 lambda 过程 `param`s 作为它的参数和 `body` 表达式作为它的主体并将其绑定到 `name`在当前环境下。 `name`必须是有效的方案符号。 每个 `param`必须是唯一的有效方案 象征。 此快捷方式等效于：
(define <name> (lambda ([param] ...) <body> ...))
```

此代码返回非空列表的长度，空列表返回 0：

```lisp
(define nums '(1 2 3))
(if (null? nums) 0 (length nums))
```

### `cond`

```lisp
(cond <clause> ...)
```

这 `clause`对应于形式的表达式

```lisp
(<test> [expression] ...)
```

或者， `clause`可以写成

```lisp
(else [expression] ...)
```

从第一个开始 `clause`. 评估 `test`. 如果为真，评估 `expression`s 按顺序，返回最后一个。 如果没有，返回什么 `test`改为评估为。 如果 `test`为假，继续下一步 `clause`. 如果没有更多 `clause`s，返回值未定义。 表格条款 `(else [expression] ...)`相当于 `(#t [expression] ...)`.

**例子：** 此代码为负数返回 -1，为正数返回 1，为零返回 0。

```lisp
(define n -3)
(cond
    ((< n 0) -1)
    ((> n 0) 1)
    (else 0)
)
```

### `let` 将符号临时绑定到值

![](./attachments/Pasted%20image%2020221002155543.png)

```lisp
(let ([binding] ...) <body> ...)
```

这 `binding`对应于形式的表达式

```lisp
(<name> <expression>)
```

首先， `expression`每个 `binding`在当前帧中进行计算。 接下来，创建一个扩展当前环境的新框架，并且每个框架 `name`绑定到其相应的评估 `expression`在里面。

**Example:** This `let` form has two bindings and three body expressions:

```lisp
(let (
      (x 5)
      (y 10)
     )
  (print x)
  (print y)
  (+ x y)
)
```

### `begin`

```
(begin <expression> ...)
```

在当前环境中 执行每个 `expression`，返回最后一个表达式的结果。

**例子：** 这里是 `begin`在里面使用 `if`在程序中形成。 返回值是三者中的最后一个表达式。

```lisp
(define (sortedpair a b)
    (if (> a b)
        (begin
            (print a)
            (print b)
            (cons a (cons b nil))
        )
        (begin
            (print b)
            (print a)
            (cons b (cons a nil))
        )
    )
)

(define spair (sortedpair 10 20))
(car spair)
```

### `lambda`

![](./attachments/Pasted%20image%2020221002155237.png)

```lisp
(lambda ([param] ...) <body> ...)
```

创建一个新的 lambda `param`s 作为它的参数和 `body`表达式 作为它的函数体。 当调用此窗体创建的过程时，调用框架 将扩展定义此 lambda 的环境。

**例子：** 此代码立即使用两个参数调用 lambda 过程：

```lisp
( (lambda(x y) (+ (* x x) (* y y))) 3 4)
```

### `quote`

```lisp
(quote <expression>)
```

或者，

```lisp
'<expression>
```

直接返回文字 `expression`， 不执行。

### `quasiquote`

```lisp
(quasiquote <expression>)
```

或者，

```lisp
`<expression>
```

返回文字 `expression`，不执行 除非一个子表达式 的 `expression`形式为：

```lisp
(unquote <expr2>)
```

在这种情况下 `expr2`被执行并替换上面的形式 否则不执行 `expression`.

### `unquote`

```lisp
(unquote <expr2>)
```

或者，

```lisp
,<expr2>
```

### `mu`

```lisp
(mu ([param] ...) <body> ...)
```

### `define-macro`

创建一个新的 mu 过程 `param`s 作为它的参数和 `body`表达式作为它的身体。 当调用此表单创建的过程时， 调用框架将扩展调用 mu 的环境。

```lisp
(define-macro (<name> [param] ...) <body> ...)
```

构造一个新的宏过程 `param`s 作为它的参数和 `body` 表达式作为它的主体并将其绑定到 `name`在当前环境下。 `name`必须是有效的方案符号。 每个 `param`必须是唯一的有效方案 象征。

宏过程应该是词法范围的，就像 lambda 过程一样。

### `expect`

```lisp
(expect <expr> <output>)
```

评估 `expr`在当前环境中并将其与（未评估的）进行比较 `output`，打印出结果。 如果在评估时发生异常 `expr`, 它被捕获并打印回溯。

### `unquote-splicing`

```lisp
(unquote-splicing <expr2>)
```

或者，

```lisp
,@<expr2>
```

如同 `unquote`， 除了那个 `expr2`必须评估为一个列表，即 然后拼接到包含它的结构中 `expression`.

### `delay`

```lisp
(delay <expression>)
```

返回一个承诺 `expression`在当前环境下进行评估。

### `cons-stream`

```lisp
(cons-stream <first> <rest>)
```

`(cons <first> (delay <rest>))` 的简写

### `set!`

```lisp
(set! <name> <expression>)
```

评估 `expression`并将结果绑定到 `name`在第一帧它可以 可以从当前环境中找到。 如果 `name`不受当前约束 环境，这会导致错误。

返回值未定义。

## Quotation

![](./attachments/Pasted%20image%2020221002155655.png)

![](./attachments/Pasted%20image%2020221002155614.png)
![](./attachments/Pasted%20image%2020221002155729.png)

- 约束你的大脑：你现在 生活在应用程序编程的世界中。 看，妈，没有突变！

## 附加阅读

- [Scheme built-ins](https://cs61a.org/articles/scheme-builtins/) - 涵盖了基于 Python 的内置程序 口译员。
- [R5RS 规范](http://www.schemers.org/Documents/Standards/R5RS/) - 61A 方案的完整方案规范 最相似。

**=, eq?, equal?**

-   `(= <a> <b>)` returns true if a equals b. Both must be numbers.
-   `(eq? <a> <b>)` returns true if a equals b and they are both numbers. For two objects, `eq?` returns true if both refer to the same object in memory.
-   `(equal? <a> <b>)` returns true if a and b are equivalent. For two pairs, they are equivalent if their cars are equivalent and their cdrs are equivalent.

```lisp
scm> (define a '(1 2 3))
a
scm> (= a a)
Error
scm> (equal? a '(1 2 3))
#t
scm> (eq? a '(1 2 3))
#f
```
