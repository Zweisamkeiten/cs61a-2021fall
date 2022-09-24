## Mutability 可变性

### Objects 对象
Python 中的每个值都是一个对象
- 所有对象都有属性
- 对象通常有关联的方法

### 列表变化

`append()` 将单个元素添加到列表中
`extend()` 将一个列表中的所有元素添加到列表中
`pop([i])` 默认移除并返回最后一个元素 Removes the item with the index _i_ from the array and returns it.
`remove()` 删除等于输入参数的第一个元素
`insert(i, x)` 在 位置 `i` 前插入 `x`
切片改变列表
```python
L = [1, 2, 3, 4, 5]

L[2] = 6

L[1:3] = [9, 8]

L[2:4] = []            # Deleting elements

L[1:1] = [2, 3, 4, 5]  # Inserting elements

L[len(L):] = [10, 11]  # Appending

L = L + [20, 30]

L[0:0] = range(-3, 0)  # Prepending
```

### 字典变化
### 元组
元组是不可变的序列
```python
empty = ()
# or
empty = tuple()
```

具有多个元素的元组
```python
conditions = ('rain', 'shine')
# or
conditions = 'rain', 'shine'
```

元组合并
```python
('come', '☂') + ('or', '☼')  # ('come', '☂', 'or', '☼')
```

检查是否包含
```python
'wally' in ('wall-e', 'wallace', 'waldo')  # True
```

切片
```python
rainbow = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
roy = rainbow[:3] # ('red', 'orange', 'yellow')
```

### 不可变与可变
不可变类型：int、float、string、tuple

### 不可变中的可变
如果不可变序列包含可变值作为元素，则它仍可能更改。
```python
t = (1, [2, 3])
t[1][0] = 99
t[1][1] = "Problems"
```

### 内容相等 和 身份id相等

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

list1 == list2 # True
list1 is list2 # False
```

### 可变的默认参数
```python
def f(s=[]):
    s.append(3)
    return len(s)

f() # 1
f() # 2
f() # 3

# 此处生成的[] 实际上在函数外被创建只是没有被绑定到外部的名字
```