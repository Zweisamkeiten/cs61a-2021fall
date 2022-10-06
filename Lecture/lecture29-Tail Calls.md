---
date created: 2022-10-03 18:43
date updated: 2022-10-03 19:15
---

# 尾调用

## Lexical vs dynamic scopes 词法和动态范围

### 词法范围

词法范围(静态范围)： 框架的父级是定义过程的框架

```lisp
(define f (lambda (x) (+ x y))) // y 的范围不能超过定义过程，因此找不到
(define g (lambda (x y) (f (+ x x))))
(g 3 7) //Error: unknown identifier: y
```

动态范围： 框架的父级是调用过程的框架
scheme `mu` 动态范围的特殊形式
![](./attachments/Pasted%20image%2020221003185312.png)

```lisp
(define f (mu (x) (+ x y))) // 去调用过程的框架去寻找 y 的值
(define g (lambda (x y) (f (+ x x))))
(g 3 7)
```

## 递归效率

![](./attachments/Pasted%20image%2020221003185430.png)
对于阶乘函数， 迭代方法空间是定值， 递归方法空间为线性增长

## 尾递归函数
Python 不支持尾调用优化，虽然下述这样的写法是标准的尾递归。
![](./attachments/Pasted%20image%2020221003195637.png)
![](./attachments/Pasted%20image%2020221003185905.png)
它好像到达退出条件，直接返回

```lisp
(define (factorial n k)
    (if (= n 0)
        k
        (factorial (- n 1) (* k n))))
```

### 什么是尾调用

尾调用的概念非常简单，一句话就能说清楚，就是指某个函数的最后一步是调用另一个函数。

```javascript
function f(x){
  return g(x);
}

// 情况一 调用g后还有其他操作 不属于
function f(x){
   let y = g(x);
	return y;
}
 
// 情况二 调用后还有加1操作 不属于
function f(x){
	return g(x) + 1;
}

```

尾调用不一定出现在函数尾部，只要是最后一步操作即可。

```javascript
function f(x) {
  if (x > 0) {
    return m(x)
  }
  return n(x);
}
```

上面代码中，函数m和n都属于尾调用，因为它们都是函数f的最后一步操作。

### 尾递归

**函数调用自身，称为递归。如果尾调用自身，就称为尾递归。**

递归非常耗费内存，因为需要同时保存成千上百个调用记录，很容易发生"栈溢出"错误（stack overflow）。但对于尾递归来说，由于只存在一个调用记录，所以永远不会发生"栈溢出"错误。

```javascript
function factorial(n) {
   if (n ===   1) return 1;
   return n * factorial(n - 1);
}
 
factorial(5) // 120
```

上面代码是一个阶乘函数，计算n的阶乘，最多需要保存n个调用记录，复杂度 O(n) 。

如果改写成尾递归，只保留一个调用记录，复杂度 O(1) 。

```javascript
 
function factorial(n, total) {
  if (n ===   1) return total;
  return factorial(n - 1, n * total);
}
 
factorial(5, 1) // 120
```

## 尾调用优化

尾调用之所以与其他调用不同，就在于它的特殊的调用位置。

我们知道，函数调用会在内存形成一个"调用记录"，又称"调用帧"（call frame），保存调用位置和内部变量等信息。如果在函数A的内部调用函数B，那么在A的调用记录上方，还会形成一个B的调用记录。等到B运行结束，将结果返回到A，B的调用记录才会消失。如果函数B内部还调用函数C，那就还有一个C的调用记录栈，以此类推。所有的调用记录，就形成一个["调用栈"](https://zh.wikipedia.org/wiki/%E8%B0%83%E7%94%A8%E6%A0%88)（call stack）。

![](./attachments/Pasted%20image%2020221003191237.png)
尾调用由于是函数的最后一步操作，所以不需要保留外层函数的调用记录，因为调用位置、内部变量等信息都不会再用到了，只要直接用内层函数的调用记录，取代外层函数的调用记录就可以了。

```javascript
function f() {
	let m = 1;
	let n = 2;
	return g(m + n);
}
f();

// 等同于
function f() {
	return g(3);
}
f();

// 等同于
g(3);
```

上面代码中，如果函数g不是尾调用，函数f就需要保存内部变量m和n的值、g的调用位置等信息。但由于调用g之后，函数f就结束了，所以执行到最后一步，完全可以删除 f() 的调用记录，只保留 g(3) 的调用记录。

这就叫做"尾调用优化"（Tail call optimization），即只保留内层函数的调用记录。如果所有函数都是尾调用，那么完全可以做到每次执行时，调用记录只有一项，这将大大节省内存。这就是"尾调用优化"的意义。

## 递归函数的改写

尾递归的实现，往往需要**改写递归函数，确保最后一步只调用自身**。做到这一点的方法，就是把**所有用到的内部变量改写成函数的参数**。比如上面的例子，阶乘函数 factorial 需要用到一个中间变量 total ，那就把这个中间变量改写成函数的参数。这样做的缺点就是不太直观，第一眼很难看出来，为什么计算5的阶乘，需要传入两个参数5和1？

两个方法可以解决这个问题。方法一是在尾递归函数之外，再提供一个正常形式的函数。

```javascript
function tailFactorial(n, total) {
  if (n === 1) return total;
  return tailFactorial(n - 1, n * total);
}

function factorial(n) {
  return tailFactorial(n, 1);
}

factorial(5) // 120
```

函数式编程有一个概念，叫做[柯里化](https://en.wikipedia.org/wiki/Currying)（currying），意思是将多参数的函数转换成单参数的形式。这里也可以使用柯里化。

```javascript
function currying(fn, n) {
  return function (m) {
    return fn.call(this, m, n);
  };
}

function tailFactorial(n, total) {
  if (n === 1) return total;
  return tailFactorial(n - 1, n * total);
}

const factorial = currying(tailFactorial, 1);

factorial(5) // 120
```

第二种方法就简单多了，就是采用ES6的函数默认值。

```javascript
function factorial(n, total = 1) {
  if (n === 1) return total;
  return factorial(n - 1, n * total);
}

factorial(5) // 120
```

总结一下，递归本质上是一种循环操作。纯粹的函数式编程语言没有循环操作命令，所有的循环都用递归实现，这就是为什么尾递归对这些语言极其重要。对于其他支持"尾调用优化"的语言（比如Lua，ES6），只需要知道循环可以用递归代替，而一旦使用递归，就最好使用尾递归。

## Python 中的类尾递归实现

Python 并不支持尾递归优化, 虽然下述是一个标准的尾递归写法

```python
def factorial(n, k):
    if n == 0:
        return k
    else:
        return factorial(n-1, k*n)
```

### Thunk: 包装在无参数函数中的表达式
```python
thunk1 = lambda: 2 * (3 + 4) // thunk1() =>  14
thunk2 = lambda: add(2, 4) // thunk2() =>  6
```

### Trampolining: 通过循环迭代调用 Thunk函数 返回的函数
```python
def trampoline(f, *args):
    v = f(*args)
    while callable(v):
        v = v()
    return v

def factorial_thunked(n, k):
    if n == 0:
        return k
    else:
        return lambda: factorial_thunked(n - 1, k * n)
        
trampoline(factorial_thunked, 3, 1)
```

这样在原来每一层将要进入递归时， 等价的直接返回填入下一层参数的函数，并进行调用，循环覆盖，直到 **Thunk** 函数返回退出条件的值。

### 程序中如何判断尾递归调用

视频这一节的 [tail calls](https://www.youtube.com/watch?v=V4HDNg79EXo&list=PL6BsET-8jgYXdYh7kYQ-4HkO_EF_BItoz&index=3) 讲述了如下判断方式：
![](./attachments/Pasted%20image%2020221005215022.png)
-   首先必须是lambda 表达式函数体的最后一个子表达式。
-   其次是if 表达式中的程序体的子表达式。
-   cond 表达式中的所有非谓词表示式（非判断部分）。
-   and, or, begin, let 的最后一个子表达式。


### Scheme 解释器中的优化实现

Thunk 类实例表示它的类成员变量 expr 需要在类成员变量 env 中被计算。

当 `optimized_eval` 接受非原子的 tail-call 表达式，它立即返回 Thunk 实例，而不是继续去递归 `scheme_eval(expr, env)` 计算表达式，而是先返回，再计算 Thunk 实例中的 expr，相当于回收之前的递归深度/空间。

否则的话，它应当反复调用 `original_scheme_eval`，直到它返回值不是 Thunk 类型。

def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in environment ENV. If TAIL,
        return a Thunk containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Thunk(expr, env)
```python
        result = Thunk(expr, env)
        # BEGIN PROBLEM 19
        "*** YOR CODE HERE ***"
        while isinstance(result, Thunk):
            result = original_scheme_eval(result.expr, result.env)
        return result
        # END PROBLEM 19
    return optimized_eval

scheme_eval = optimize_tail_calls(scheme_eval) # uncomment this!
```

遵循尾递归调用判断规则，设置 optimize_tail_calls 的第三个参数 `tail` 为 True。

-   lambda, cond, let, begin 涉及 `eval_all`。
-   if 涉及 `do_if_form`。
-   and, or 分别是 `do_and_form`, `do_or_form`。
```python
def eval_all(expressions, env):
    # BEGIN PROBLEM 7
    # return scheme_eval(expressions.first, env) # replace this with lines of your own code
    value = None
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        expressions = expressions.rest
    return value
    # END PROBLEM 7

def do_if_form(expressions, env):
    validate_form(expressions, 2, 3)
    if is_true_primitive(scheme_eval(expressions.first, env)):
        return scheme_eval(expressions.rest.first, env, True)
    elif len(expressions) == 3:
        return scheme_eval(expressions.rest.rest.first, env, True)

def do_and_form(expressions, env):
    # BEGIN PROBLEM 12
    value = True
    "*** YOUR CODE HERE ***"
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        if value is False:
            return False
        expressions = expressions.rest
    return value

def do_or_form(expressions, env):
    # BEGIN PROBLEM 12
    "*** YOUR CODE HERE ***"
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        if value is not False:
            return value
        expressions = expressions.rest
    return False
    # END PROBLEM 12
```

```
