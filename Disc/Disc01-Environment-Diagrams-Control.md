---
date created: 2022-04-22 22:51
---

# Disc 1 Control and Environments

## Control [[lecture03-Control#control)

### If statements

```python
if <conditional expression>:
	<suite of statements>
elif <conditional expression>:
	<suite of statements>
else:
	<suite of statements>
```

- 只有在遇到的第一个 `if` 或 `elif` 下的条件表达式为真下缩进的 `suite` 会被执行
- 如果没有条件表达式为真值, 则 `else` suite 会被执行.
- 一个条件语句只有一个 `else` 分支

## Bollean Operators

- 要注意 `and` 和 `or` 的短路特性
- 其会返回最后一个被计算的操作数的结果值, 因此 `and` `or` 的返回值不一定全是 `True` 和 `False`

## Environments Diagrams

环境图 是用来跟踪所有被定义的变量和他们所绑定的值.

### Assignment Statements

`x = 3`

1. 计算值表达式位于 `=` 号右侧的值
2. 在当前帧 (frame) 中写入变量名和表达式的值

### def Statements

- `def statements` 创建函数对象然后将其绑定到一个变量 `name`.
- 记录函数名以及绑定函数对象到变量, 重要的是记录函数的 `parent frame` 父帧, 因为这是它被定义的地方
- 更重要的是: 对于 `def statements` 的赋值 使用的是指针 函数名`name` 指向实际的函数对象, 这与 `primitive assignments` 的行为是不同的
  - `primitive assignments` 不能拆开理解, 它应该是一个专用词组. 对应 `objective assignments`.
  - 原始赋值 例如 `int a = 4; int b = a; b = 3;` 虽然b的值改变了, 但 a 仍为 `4`, 因此原始赋值对于变量来说是将值复制到另一个原始变量. 而对象赋值, 两个变量都为对一个 **可变对象** 的引用, 两者都能看到其对象的变化.
  - 因此我理解这句 `Assignments for def statements use pointers to functions, which can have different behavior than primitive assignments.` 其意思为比较 python 与 C, 前者def func(): func其实是一个 name, 它是对实际函数对象的引用名, 而 C 中的 func 实际上是在编译器中解释为函数的入口地址的全局声明, 它是一个原始类型.
### Call Expressions  
Call expressions, such as square(2), apply functions to arguments. When exe-  
cuting call expressions, we create a new frame in our diagram to keep track of local  variables. 