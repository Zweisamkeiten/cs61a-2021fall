---
date created: 2022-09-14 20:34
---

## Data abstractions

程序中的许多值都是复合值。数据抽象使得我们可以将复合值作为一个完整的单元而无需担心值的内部储存方式。

构造函数 Constructor
选择器 Selector

![](./attachments/Pasted%20image%2020220914201627.png)

违反抽象的原则： 即设计函数时假定输入值的构成方式

## 字典

```python
>>> words["pavo"]
KeyError: pavo

>>> words.get("pavo", "🤔")
'🤔'
```

如果 _key_ 存在于字典中则返回 _key_ 的值，否则返回 _default_。 如果 _default_ 未给出则默认为 `None`，因而此方法绝不会引发 [`KeyError`](https://docs.python.org/zh-cn/3.10/library/exceptions.html#KeyError "KeyError")。

key 不可为任意可变对象

value 可以为任意值

字典迭代

```python
insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])

>>> 8 100 6
```

字典推导式

```python
{key: value for <name> in <iter exp>}
```

```python
def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which
    match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
```