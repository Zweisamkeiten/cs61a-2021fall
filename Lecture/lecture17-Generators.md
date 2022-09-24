---
date created: 2022-09-16 13:45
date updated: 2022-09-16 16:16
---

## Generators

生成器使用 `yield` 代替 `return`

```python
def evens():
	num = 0
	while num < 10:
		yield num
		num += 2
```

生成器是一种类型的迭代器，从一个生成函数中产生结果

```python
evengen = evens()

next(evengen)  # 0
next(evengen)  # 2
next(evengen)  # 4
next(evengen)  # 6
next(evengen)  # 8
next(evengen)  # ❌ StopIteration exception
```

## How generators work 生成器是如何工作的

```python
def evens():
    num = 0
    while num < 2:
        yield num
        num += 2

gen = evens()

next(gen)
next(gen) # 这个就无法返回 num 值了 会出现报错
```

- 当函数被调用，python立即返回一个迭代器但不进入执行函数
- 每当 对迭代器的 `next()` 被调用, 这会执行生成函数的函数体直到下一个停靠点 `yield` 语句所在处。 第一次调用即是停到第一个 `yield`
- 如果它发现了一个 `yield` 语句，它在下一条语句开始前暂停并返回产生值
- 如果它无法到达 `yield` 语句, 它会在函数末尾停止并引发一个 `StopIteration` 意外

## 可以对生成器使用循环遍历

因为生成器也是一种特殊的迭代器

```python
def evens(start, end):
    num = start + (start % 2)
    while num < end:
        yield num
        num += 2

for num in evens(12, 60):
   print(num)
```

looks like...

```python
evens = [num for num in range(12, 60) if num % 2 == 0]
# Or  = filter(lambda x: x % 2 ==0, range(12, 60))
for num in evens:
	print(num)
```

## 为什么使用生成器

生成器是懒惰的，它只会在需要下一个元素的时候生成下一元素。
巨大的列表会导致程序用完全部内存

## 可迭代的 Yielding from

`yield from` 关键字语句可以用于从一个可迭代对象中产生一个值当需要的时候

```python
def a_then_b(a, b):
    for item in a:
        yield item
    for item in b:
        yield item

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))

# yield from 替代方案
def a_then_b(a, b):
    yield from a
    yield from b

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))
```

## Yielding from generators

```python
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
```

![[Pasted image 20220916161602.png]]

## Generator function with return

当一个生成器函数执行到 `return` 语句, 它将退出并不产生更多的值

```python
def f(x):
	yield x
	yield x + 1
	return 
	yield x + 3
list(f(2)) # [2, 3]
```

python 允许其可以返回一个值， 但是该值无法被产生

```python
def g(x):
	yield x
	yield x + 1
	return x + 2
	yield x + 3
list(g(2)) # [2, 3]
# 但也有办法访问到其返回值
def h(x):
	y = yield from g(x)
	yield y
list(h(2)) # [2, 3, 4]
```


