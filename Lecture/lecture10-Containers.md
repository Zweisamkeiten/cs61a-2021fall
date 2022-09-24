---
date created: 2022-09-14 10:17
---

- Lists 列表

```python
members = ['Pamela', 'tinu', 'brenda', 7, 8]
```

可以放置任意python值, 可不同类型混用
`len()`

```python
form operator import getitem
getitem(letters, 0)
# 等价
letters[0]

# 列表拼接
all = listA + listB

# 等价
from operator import add
all = add(listA, listB)

# 列表重复
b = [1, 2, 3]
c = b * 3

# 等价
from operator import mul
c = mul(b, 3)
```

![](./attachments/Pasted%20image%2020220914100512.png)

- Containment

使用 `in` 操作符来测试某值是否存在该容器中

```python
digits = [1, 2, 3]
1 in digits
```

- For statement

For 循环语句的执行过程

```python
for <name> in <expression>:
    <suite>
```

```
1. 先计算出 `<expression>`, 必须产生一个可以迭代的值(一个序列)
2. 对于序列中的每个值
	1. 绑定 `<name>` 到当前帧中的元素
	2. 执行 `<suite>`
```

```python
pairs = [[1, 2], [2, 2], [3, 2], [4, 4)
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1
# x, y会将其中嵌套的列表拆分开 每次循环 等价于 x, y = [1, 2] =>  x = 1, y = 2
```

![](./attachments/Pasted%20image%2020220914101508.png)

- range

`range(-2, 3)` => [-2, 3) 左闭右开
`range(6)` => [0, 6)

- List comprehensions 列表推导式

```python
[<map exp> for <name> in <iter exp>]
[<map exp> for <name> in <iter exp> if <filter exp>]
```

-   Add a new frame with the current frame as its parent
-   Create an empty result list that is the value of the expression
-   For each element in the iterable value of `<iter exp>`:
    -   Bind `<name>` to that element in the new frame from step 1
    -   If `<filter exp>` evaluates to a true value, then add the value of `<map exp>` to the result list
![](./attachments/Pasted%20image%2020220914102931.png)