---
date created: 2022-09-17 10:15
date updated: 2022-09-17 11:19
---

## 面向对象编程

OOP 是一种构成程序的方法包含以下:

- 数据抽象 Data abstraction
- 将信息与对应行为相绑定

一种计算的隐喻 使用分布式的状态

- 每个对象都有其本地状态
- 每个对象都知道如何管理其自身的本地状态，通过调用自身的方法
- 对象间传递信息的方式通过方法调用
- 一些不同的对象可能是同一个类型的不同实例
- 不同的类型可能互相关联 继承

## OOP 术语

- 类: Class 定义新的数据类型的模版
- 对象: Object 类的实例
- 实例变量: Instance variables 每个对象都有数据属性
- 方法: Methods 每个对象有函数属性称作方法

## Classes 类

```python
# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

    def reduce_inventory(self, amount):
        self.inventory -= amount

    def get_label(self):
        return "Foxolate Shop: " + self.name

    def get_inventory_report(self):
        if self.inventory == 0:
            return "There are no bars!"
        return f"There are {self.inventory} bars."
```

```python
# 类实例化： 对象构造
# Product(args) 作为构造器
pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])

# 方法调用
pina_bar.increase_inventory(2)
```

**构造器** `constructor` 被调用:

- 对应类的一个新实例被创建
- `__init__` 方法被调用 使用新对象作为第一个参数 (named `self` ) 为对象属性值初始化

**实例变量**

- 描述对象的状态
- 对象的方法可以更改这些变量的值或者分配新变量

```python
pina_bar.increase_inventory(2)

# 等价
Product.increase_inventory(pina_bar, 2)
```

```python
class Product:
    def increase_inventory(self, amount):
        self.inventory += amount
```

`self` 被预先绑定到 `pina_bar`

**点符号**

- 所有对象属性可以通过 点符号来访问

## 动态属性 Dynamic attributes

- Class 语句创建一个新类并在 **当前帧环境** 中将该类绑定到类名
- 内部 `def` 语句创建类的属性 而不是在帧中创建 names
- 类的新的属性绑定也可以通过除 `__init__` 的方法创建

## 类变量 Class variables

A **class variable** is an assignment inside the class that isn't inside a method body. 类变量是在类内部进行赋值分配，而不是在方法体内

```python
class Product:
    sales_tax = 0.07

    def get_total_price(self, quantity):
        return (self.price * (1 + self.sales_tax)) * quantity

pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
truffle_bar = Product("Truffalapagus", 9.99,
    ["170 calories", "19 g sugar"])

pina_bar.sales_tax
truffle_bar.sales_tax
pina_bar.get_total_price(4)
truffle_bar.get_total_price(4)
```

类变量在所有的示例之间共享，因为他是类的属性，而不是实例

```python
Product.sales_tax = 1 # 会使得已经创建的实例的sales_tax 都改变，并影响将来创建的

# or
pina_bar.sales_tax = 1 # 实例新建了实例属性覆盖了 原来的类属性, 因此 再改变 Product.sales_tax 也不会影响它，它自己改变也不会影响原来的类属性
```

## Accessing attributes

`getattr` 和点表达式作用相同

```python
getattr(pina_bar, 'inventory')   # 1
hasattr(pina_bar, 'reduce_inventory')  # True
```

## Public vs. Private

### Attributes are all public

- 可访问和改变对象的任意属性
- 甚至可以赋予一个新的实例变量

```python
pina_bar.brand_new_attribute_haha = "instanception"
```

### Private attributes

use this convention(约定) 来表示属性的访问级别

- `__` (两个下划线) 在非常私有的属性名前
- `_` (一个下划线) 在半私有的属性名前
- 没有下划线在公开属性名前

这将允许类隐藏实现细节和增加额外的错误检查
