---
date created: 2022-10-03 10:23
date updated: 2022-10-03 10:47
---

## 编程语言

`高级编程语言(Python, C++, Js)` => 汇编语言(特定于硬件) => 机器语言(特定于硬解)

高级语言:

- 提供抽象的方法， 命名，函数定义和对象
- 抽象出系统细节以独立于硬件和操作系统
- 语句和表达式要么由另一个程序解释，要么编译翻译成低级语言

### 编译和解释

- 编译： 源代码被翻译成机器代码，代码可以重复分发和运行
  - Source code => Compiler => Machine code => Output
- 解释： 一个解释器直接运行源代码 无需先编译
  - Source code => Interpreter => Output
  - 在最流行的实现 (CPython) 中， python 程序被解释，但是有一个编译步骤
    - Source code => Compiler => Bytecode => Virtual Machine => Output

### 解释器/编译器阶段步骤

- Source code => Lexing => Parsing => Abstract Syntax Tree
- 源代码 => 词法 => 语法分析 => 抽象语法树

### 词法 分析

- 解析语言的任务涉及转换表达式的字符串表示 到表示表达式的结构化对象中。

- ![](./attachments/Pasted%20image%2020221003103207.png)

- ![](./attachments/Pasted%20image%2020221003103428.png)

- `' (* 4 5.6))'`→ `'('`, `'*'`, `4`, `5.6`, `')', ')'`
  - 迭代过程
  - 检查格式错误的令牌
  - 确定令牌的类型
  - 一次处理一行

### 语法分析 Syntactic analysis

`'('`, `'+'`, `1`, ... → `Pair('+', Pair(1, ...))`

- Tree-recursive process 树递归过程
- Balances parentheses 平衡括号
- Returns tree structure 返回树结构
- Processes multiple lines 处理多行

## 计算器语言

### 什么是编程语言:

- 语法： 语言中的规则声明和表达
- 语义： 语句和表达式的执行和计算规则
- 规范： 描述语言的精确语法和语义文档
- 规范实现： 语言的解释器或编译器

![](./attachments/Pasted%20image%2020221003104226.png)
![](./attachments/Pasted%20image%2020221003104251.png)

## 评估语言

`eval` 函数计算表达式的值
泛型函数， 根据表达式的类型(原始或调用) 运行

`apply` 函数将操作应用与参数列表
`apply(op, args)`

## 交互式解释器

### REPL：读取-评估-打印循环

许多编程语言的用户界面是交互式解释器

- 打印提示
- 读取用户输入的文本
- 将文本输入解析为表达式
- 评估表达式
- 如果发生任何错误，请报告这些错误，否则
- 打印表达式的值并重复

### 引发异常

在词法分析、句法分析、评估和应用期间可能会引发异常。

示例异常

- **词法分析** ：Token 2.3.4 引发 `ValueError("invalid numeral")`
- **句法分析** ：一个额外的 `)` raises `SyntaxError("unexpected token")`
- **Eval** : 空组合引发 `TypeError("() is not a number or call expression")`
- **Apply** : No arguments to - raises TypeError("- requires at least 1 argument")

### 处理异常

交互式解释器打印有关每个错误的信息。

一个设计良好的交互式解释器不应该在错误时完全停止， 使用户有机会在当前环境中再次尝试。
