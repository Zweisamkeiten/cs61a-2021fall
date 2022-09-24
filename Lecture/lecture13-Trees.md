---
date created: 2022-09-14 20:54
---

![[Pasted image 20220914204303.png]]

![[Pasted image 20220914204738.png]]

等价

```python
def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)
```
