---
date created: 2022-09-15 17:50
date updated: 2022-09-16 14:10
---

## Iterators

迭代器提供对值的逐个顺序访问, 它是一个可以记住遍历位置的对象

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

`iter(iterable)` 返回一个可迭代元素的迭代器
`next(iterator)` 返回迭代器的下一个元素

```python
toppings = ["pineapple", "pepper", "mushroom", "roasted red pepper"]

topperator = iter(toppings)
next(iter) # 'pineapple'
next(iter) # 'pepper'
next(iter) # 'mushroom'
next(iter) # 'roasted red pepper'
next(iter) # ❌ StopIteration exception
```

![[Pasted image 20220915175714.png]]
每次调用都生成新迭代器

`iter()` can return an iterator for any iterable object.

```python
my_order = ["Yuca Shepherds Pie", "Pão de queijo", "Guaraná"]
order_iter = iter(order)
next(order_iter)  # "Yuca Shepherds Pie"

ranked_chocolates = ("Dark", "Milk", "White")
chocolate_iter = iter(ranked_chocolates)
next(chocolate_iter)  # "Dark"

best_topping = "pineapple"
topping_iter = iter(best_topping)
next(topping_iter) # "p"

scores = range(1, 21)
score_iter = iter(scores)
next(score_iter) # 1
```

对字典生成迭代器

```python
prices = {"1": 1, "2": 2, "3": 3}
price_iter = iter(prices.keys())
next(price_iter)  # "pineapple"

price_iter = iter(prices.values())
next(price_iter)  # 9.99

price_iter = iter(prices.items())
next(price_iter)  # ("pineapple", 9.99)
```

### 循环遍历迭代器

```python
# 在 for 循环中使用时，Python 将调用 `next()`在迭代器上 在每次迭代中：
nums = range(1, 4)
num_iter = iter(nums)

for num in num_iter:
	print(num)
```

```python
# 对已使用的迭代器的循环
nums = range(1, 4)
num_iter = iter(nums)
first = next(num_iter)

for num in num_iter:
    print(num)
# 会从第一个之后的num开始输出
```

迭代器是可变的，一旦迭代器向前移动就不会返回之前的值

### 有用的内置函数

`list(iterable)` 返回一个包含所有项目的列表 `iterable`
![[Pasted image 20220915180909.png]]
`tuple(iterable)` 返回一个包含所有项目的元组 `iterable`
`sorted(iterable)` 返回一个包含所有项目的排序列表 `iterable`
`reversed(sequence）` 遍历项目 `sequence` 以相反的顺序
![[Pasted image 20220915181204.png]]
`zip(*iterables)` 使用合并来自每个可迭代对象
![[Pasted image 20220915181336.png]]
`map(func, iterable, ...)`  使用 `func(x)` 作用在 迭代器中的每个 `x`, 返回的为迭代器
等同于 [func(x) for x in iterable]

`filter(func, iterable` 迭代每一个 迭代器中的 `x` 如果 `func(x)` == `True` 筛选出来 返回的是迭代器
等同于 [x for x in iterable if func(x)]

![[Pasted image 20220915183012.png]]

`reduce(f, iterable)`- 必须与 `functools`. 应用两个参数的函数 `f`累计到项目 `iterable`，从左到右，从而将序列缩减为单个值。
例如 `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` calculates `((((1+2)+3)+4)+5)`
## 使用迭代器的原因

使用迭代器可使得减少对数据本身的假设。

迭代器将一个序列和一个位置与该序列捆绑在一个对象中。 将该对象传递给另一个函数始终保留其位置。 确保序列的每个元素只处理一次。 将可以执行的操作限制为仅调用 next()。
