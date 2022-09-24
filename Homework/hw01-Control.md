---
date created: 2022-04-22 11:17
---

1. 函数名其实以指向一个函数对象的引用, 因此可以将函数名附给一个 `name` 变量, 使得该函数对象现在有两个不同 `name` 的引用. 相当于别名

```python
>>> a = abs # 变量 name a 指向 abs 函数
>>> a(-1) # 因此可用 a 调用 abs 函数
1
```

```python
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
```

因此 Q2 中, 通过条件判断 b 的正负值, 使得 `f` 会指向不同函数对象的引用, 最后返回调用 `f` 传入 `a, b` 的值得出结果

2. If Function vs Statement

Q5 的重点是 **区分** `if` 语句与 行为近似与 `if` 的 `if_function`, 要点是区别 `if statements` 和 `call expressions`(调用语句)
![](./attachments/Pasted%20image%2020220422111428.png)
![](./attachments/Pasted%20image%2020220422110921.png)
调用函数时, 它传入函数的参数都是计算完成的值, 因此当函数的参数包含调用函数的表达式时, 它会先将所有参数项中的调用表达式计算完成将其返回结果作为传入该参数的值.
在此题中, `trun_func` 和 `false_func` 很明显其函数体只是一条 `print` 语句, 因此它们函数的返回值是 `None`
所以, `with_if_statement` 函数中通过 `cond()` 条件判断走其中一分支, 执行了其中一个函数, `print` 了一条
而 `with_if_function` 函数, 它的调用语句是先将其所有的参数中的 `调用表达式` 执行完成返回结果传入 `with_if_function`, 相当与在完成调用 `with_if_function` 前, `true_func`, `false_func` 已经调用完成 `print` 完成, 相当于 最后语句为 `with_if_function(True/False, None, None)` ^344d2f
[[lab01-Variables-Functions-Control#Call expression 调用表达式)