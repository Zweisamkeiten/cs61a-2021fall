---
date created: 2022-09-19 09:31
date updated: 2022-09-19 10:24
---

## 继承

### Motivation 动机

![](./attachments/Pasted%20image%2020220919092620.png)
对于含有相同属性的不同类， 为了避免重复代码，我们可以使用继承类

### Inheritance 继承

Base classes and subclasses
![](./attachments/Pasted%20image%2020220919093203.png)
**superclass**

```python
class Panda(Animal):
```

**simplest subclass** override nothing

```python
class AmorphousBlob(Animal):
	pass
```

可以重写属性 和 方法

如果子类重写了方法，python会使用子类的定义代替其父类定义

在子类中引用父类方法, 可以使用 `super()` et: `super().eat(food)`

![](./attachments/Pasted%20image%2020220919095256.png)

`super()` 是更好的风格，但是相比较慢

`super().__init__()` 也可以重写

### Multiple Inheritance 多重继承

![](./attachments/Pasted%20image%2020220919095822.png)
所有的对象都隐式继承自 `object`
![](./attachments/Pasted%20image%2020220919095913.png)
![](./attachments/Pasted%20image%2020220919095939.png)
![](./attachments/Pasted%20image%2020220919101918.png)

### Identity

`exp0 is exp1` 如果两个对象为同一个，则返回 `True`

### Composition 组合

![](./attachments/Pasted%20image%2020220919102358.png)
![](./attachments/Pasted%20image%2020220919102449.png)
