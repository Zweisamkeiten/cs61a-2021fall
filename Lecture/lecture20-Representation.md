---
date created: 2022-09-19 10:29
date updated: 2022-09-19 12:49
---

## 表示

### String formatting 字符串格式化

之前一直使用 `+` 运算符来表示字符串串联

- 加号容易弄错
- 比较难理解最后的字符串是什么
- 明确要求 `str()` 是非字符串

#### **String interpolation** 字符串插值

组合字符串文字的过程和表达式的结果
只需放一个 `f` 在引号前 然后将任何有效的 Python 表达式放在大括号内

```python
artist = "Lil Nas X"
song = "Industry Baby"
place = 2

print(f"Debuting at #{place}: '{song}' by {artist}")
```

### 对象

- repr/str representation 表示

- Special method names 特殊方法名称

- Polymorphism 多态性

- Generics 泛型

![](./attachments/Pasted%20image%2020220919103504.png)
![](./attachments/Pasted%20image%2020220919103512.png)
![](./attachments/Pasted%20image%2020220919103525.png)
![](./attachments/Pasted%20image%2020220919103545.png)
![](./attachments/Pasted%20image%2020220919104006.png)
![](./attachments/Pasted%20image%2020220919104245.png)

![](./attachments/Pasted%20image%2020220919104818.png)
![](./attachments/Pasted%20image%2020220919105007.png)
![](./attachments/Pasted%20image%2020220919105019.png)
![](./attachments/Pasted%20image%2020220919105033.png)

### 特殊方法

![](./attachments/Pasted%20image%2020220919105102.png)
![](./attachments/Pasted%20image%2020220919105212.png)
![](./attachments/Pasted%20image%2020220919105239.png)

### 多态函数

![](./attachments/Pasted%20image%2020220919105515.png)
`str()` 与 `__str__`, `repr()` 与 `__repr__`
str()在其参数上调用 `__str__`
repr() 在其参数上调用 `__repr__`

但 `repr()` 比调用 `__repr__` 要复杂: 实例的 ` __repr__  ` 属性会被忽略. 只有类属性会被发现

`str()` 也是复杂的:

- 实例的 `__str__` 属性被忽略
- 如果 `__str__` 属性没有找到, 使用 `repr` 字符串
- `str` 是一个类 而不是一个函数
- ![](./attachments/Pasted%20image%2020220919120731.png)

### 泛型

**泛型函数** 可以用于不同类型的参数

```python
def sum_two(a, b):
	return a + b
```

**类型调度** type dispatching
制作泛型函数的另一种方法是根据参数的类型选择行为

**类型强制**  type coercion
制作泛型函数的另一种方法是根据参数转换为所需要的类型
