---
date created: 2022-09-19 12:49
date updated: 2022-09-19 12:54
---

## Recursive Objects

### Linked Lists 链表

为什么需要一个新列表

python 列表被实现为动态数组, 可能不是所有情况的最佳选择

insert 元素很慢, 尤其在列表最前面附近的 因为需要移动后续的元素

加上插入太多元素可能需要在内存中重新创建整个列表， 如果超过了预先分配的内存。

**链表** listed list

![[Pasted image 20220919125604.png]]

### Link class

```python
class Link:
	enpty = ()

	def __init__(self, first, rest=empty):
		self.first = first
		self.rest = rest

ll = Link("A", Link("B", Link("C")))
```

**更高级的链表**

```python
class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
```

### 变化链表 Mutating Linked lists
![[Pasted image 20220919131143.png]]
![[Pasted image 20220919131203.png]]
![[Pasted image 20220919131314.png]]

### Tree class
![[Pasted image 20220919131326.png]]![[Pasted image 20220919131358.png]]

### 递归对象
![[Pasted image 20220919131420.png]]