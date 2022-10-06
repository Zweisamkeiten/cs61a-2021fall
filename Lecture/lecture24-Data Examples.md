---
date created: 2022-10-01 15:44
date updated: 2022-10-01 16:00
---

# Data Examples 数据结构例子

## 链表

```python
def ordered(s, key=lambda x: x):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif s.first > s.rest.first:
        return False
    else:
        return ordered(s.rest)
```

![](./attachments/Pasted%20image%2020221001155017.png)
![](./attachments/Pasted%20image%2020221001155028.png)
