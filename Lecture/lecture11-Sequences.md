---
date created: 2022-09-14 18:38
---

## Box + Pointer

列表表示为一行带有索引标签的相邻框，每个元素一个
每个框(box)包含原始值或者指向一个复合值

```python
worst_list = [ [1, 2],
               [],
               [ [3, False, None],
                 [4, lambda: 5]]]
```

## Slicing 切片

```python
letters = ["A", "B", "C", "D", "E", "F"]
        #   0    1    2    3    4    5

sublist1 = letters[1:]    # ['B', 'C', 'D', 'E', 'F']
sublist2 = letters[1:4]   # ['B', 'C', 'D']
```

切片可作为复制列表的功能

```python
listA = [2, 3]
listB = listA

listC = listA[:]
listA[0] = 2
listB[1] = 3
```

![](./attachments/Pasted%20image%2020220914182618.png)

```python
listA = [2, 3]
listB = listA

listC = list(listA)
listA[0] = 2
listB[1] = 3
```

![](./attachments/Pasted%20image%2020220914182847.png)

切片逆序
切片形如 list[begin_idx: end_idx: step] 则 list[::-1]可以逆序输出

### Functions that process iterables

The following built-in functions work for sequence types (lists, strings, etc) and any other **iterable** data type.

Function

Description

`sum(iterable, start)`

Returns the sum of values in `iterable`, initializing sum to `start`
返回迭代对象的总和值, 起始值为 `start`, 即最后还要加上start

[`all(iterable)`](https://docs.python.org/3/library/functions.html#all)

Return `True` if all elements of `iterable` are true (or if `iterable` is empty)
返回 `True` 如果迭代对象中的所有元素都为 `True` 或者迭代对象为空

[`any(iterable)`](https://docs.python.org/3/library/functions.html#any)

Return `True` if any element of `iterable` is true. Return `False` if `iterable` is empty.
返回 `True` 如果迭代对象中某一元素为 `True`. 如果迭代对象为空，则返回 `False`

`max(iterable, key=None)`

Return the max value in `iterable`
返回迭代对象中的最大值, 根据 key的规则 [[02-cats#^1d28df]]
`min(iterable, key=None)`

Return the min value in `iterable`
