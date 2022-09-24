---
date created: 2022-09-15 09:43
---

## arm-length 递归违规

```python
def min_depth(t):
    """A simple function to return the distance between t's root and its closest leaf"""
    if is_leaf(t):
        return 0 # Base case---the distance between a node and itself is zero
    h = float('inf') # Python's version of infinity
    for b in branches(t):
        if is_leaf(b): return 1 # !!!
        h = min(h, 1 + min_depth(b))
    return h
```

`!!!` 标注行是一次违规递归， 因为多做了下一级递归完成的工作。已有一个if语句来处理输入 `min_depth` 的节点是否是叶子节点

```python
def min_depth(t):
    """A simple function to return the distance between t's root and its closest leaf"""
    if is_leaf(t):
        return 0
    h = float('inf')
    for b in branches(t):
        # Still works fine!
        h = min(h, 1 + min_depth(b))
    return h
```

Arms-length 递归不仅是多余的，而且经常使我们的代码复杂化并模糊递归函数的功能，从而使编写递归函数变得更加困难。 我们总是希望我们的递归案例处理一个且只有一个递归级别。
