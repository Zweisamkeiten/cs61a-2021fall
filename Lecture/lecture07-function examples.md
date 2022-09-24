---
date created: 2022-09-12 20:21
date updated: 2022-09-12 20:24
---

## Currying

**Currying**: 将一个接收多个参数的函数转换为一次只逐个接收一个参数。

```python
def curry2(f):
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g
```

```python
from operator import add

make_adder = curry2(add)
make_adder(2)(3)
```

等价于:

```python
curry2 = lambda f: lambda x: lambda y: f(x, y)
```

currying 常见于函数式编程语言, Haskel or Clojure

## Decorators 装饰器
```python
def trace1(f):
    """
    >>> square = lambda x: x * x
    >>> trace1(square)(3)
    -> 3
    <- 9
    9
    """

    def traced(x):
        print("->", x)
        r = f(x)
        print("<-", r)
        return r

    return traced


@trace1
def square(x):
    return x * x
```

该装饰器用法等效于:
```python
square = trace1(square)
```

通用装饰器语法
```python
@ATTR
def aFunc(...):
	...

# 等价于

def aFunc(...):
	...
aFunc = ATTR(aFunc)

# ATTR 可以是任意表达式，不仅仅一个为一个函数名
```