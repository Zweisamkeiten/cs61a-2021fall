---
date created: 2022-04-22 11:22
date updated: 2022-04-22 21:09
---

# Lab 1: Vairables & Functions, Control

## Using OK

使用 Ok 运行 doctests 指定函数，运行以下命令：

```shell
python3 ok -q <specified function>
```

默认情况下，只会显示未通过的测试。 您可以使用 `-v` 显示所有测试的选项，包括您已通过的测试：

```shell
python3 ok -v
```

您还可以通过编写来使用 OK 中的调试打印功能

```shell
print("DEBUG:", x)
```

最后，当你完成所有问题时 [lab01.py](https://inst.eecs.berkeley.edu/~cs61a/fa20/lab/lab01/lab01.py) ，您必须使用 `--submit`选项：

```shell
python3 ok --submit
```

## Topic

### Division 除法

1. True Division: `/`(decimal division), `>>> 1/ 5` 真除法, 结果是浮点数
2. Floor Division: `//`(integer division) `>>> 1 // 5` 整除法, 结果为向下取整的除法
3. Modulo: `%`(remainder) `>>> 1 % 5` 模除,  结果为整除后的余数
4. 上述三种除法当遇到除数为零时都会触发 `ZeroDivisionError`, 零除数错误

`%` 可以用来检查一个数是否可以被整除

```python
x % y == 0
```

### Function 函数

当一系列的语句需要被反复执行时, 可以通过抽象方法, 将几条一系列的语句抽象为一个函数来避免出现重复的代码.

函数 接受 **参数(argument)** 并将返回 **结果(result)**

通过 `调用(call)` 来完成操作

将某些函数应用在一个函数的参数中是通过调用表达式. [[hw01-Control#^344d2f]]

#### Call expression 调用表达式

调用表达式应用一个函数，该函数可能接受也可能不接受 **参数**。 调用表达式计算为函数的返回值。

函数调用的语法：

```
  add   (    2   ,    3   )
   |         |        |
operator  operand  operand
```

每个调用表达式都需要一组括号来分隔它的 逗号分隔的操作数。

评估函数调用：

1. 计算运算符，然后计算操作数（从左到右）。
2. 将运算符应用于操作数（操作数的值）。

如果一个操作数是一个嵌套调用表达式，那么这两个步骤是 首先应用于该内部操作数再计算外部操作数。

#### `return`, `print`

当 Python 执行一个 `return`语句，函数立即终止。 如果 Python 到达函数体的末尾而不执行 `return` 语句，它会自动返回 `None`.

相比之下， `print`函数用于在终端中显示值。 这可能会导致一些混淆 `print`和 `return`因为调用 Python 解释器中的函数将打印出函数的返回值。

然而，不同于 `return`语句，当 Python 计算一个 `print` 表达式，函数不会 _立即_ 终止。

### Control 控制

#### 布尔运算符 bool

`and`, `or`, `not`
**重点** 是需要了解其短路操作
[[lecture03-Control#2 short-circuit evaluation]]

- `and`, 语句只有在两个操作数的计算结果都为 `True` 时才返回 `True`. 如果其中一个操作数结果为 `False`, 其 `and` 的计算结果为 `False`
- `or`评估为 `True`如果至少一个操作数计算为 `True`. 如果两个操作数都是 `False`， 然后 `or`评估为 `False`.
- `not`评估为 `True`如果它的操作数计算为 `False`. 它评估 到 `False`如果它的操作数计算为 `True`.

```python
>>> True and not False or not True and False
===
>>> (True and (not False)) or ((not True) and False)
```

- `not`优先级最高
- `and`
- `or` 最低优先级

`0`, `None`, `''`(空字符串), `[]`(空列表) 被视为 `False`
其余都为 `True`

短路

| Operator | Checks if:                | Evaluates from left to right up to: |
| -------- | ------------------------- | ----------------------------------- |
| AND      | All values are ture       | The first false value               |
| OR       | At lest one value is true | The first true value                |

当运算符到达允许他们对表达式作出结论的操作数时，就会发生短路。 例如， `and`一旦达到第一个假值，它就会短路，因为它知道并非所有值都是真的。`or` 一旦达到第一个真值, 就就短路
如果表达式未发生短路, 则该表达式返回最后一个操作数的值. 因此 `and` and `or` 不总是返回布尔值当使用除 `True` `False` 之外的值
![](./attachments/Pasted%20image%2020220422194315.png)

#### If statements

[[lecture03-Control#3 conditional statement 条件语句]]

```python
if x > 3:
	return True
else:
	return False
```

等价于 `return x > 3`, 这样更为简明扼要

### 错误信息

| Error Types       | Descriptions                             |
| ----------------- | ---------------------------------------- |
| SyntaxError       | 包含不正确的语法（例如，在 `if`声明或忘记关闭括号/引号）          |
| IndentationError  | 包含不正确的缩进（例如，函数体的缩进不一致）                   |
| TypeError         | 尝试对不兼容的类型进行操作（例如尝试添加函数和数字）或使用错误数量的参数调用函数 |
| ZeroDivisionError | 试图将零作为除数                                 |
