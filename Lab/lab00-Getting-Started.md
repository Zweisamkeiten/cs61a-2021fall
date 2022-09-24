---
date created: 2022-04-22 10:34
---

# Lab0: Getting Start

1. Python 环境的安装
2. Text editor
3. Python Interpreter
4. Orgnizing files
   1. 整个课程项目可构建为 `hw`, `project`, `lab`

## Python Basices

### Expressions and statements

表达式与语句
`表达式`: 是一段代码片段, 其计算结果是某个值
`语句`: 是一行或多行代码使得程序中发生某些事情

### Primitive expressions

`原始表达式`: 是只用通过一步计算得出的表达式
如

```python
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

### Arithmetic expressions

`算术表达式`: 数字使用数学算术运算符形成复合表达式, `+`, `-`, `*`, `**`, `/`, `//`, `%`

### Assignment statements

`赋值语句`: 赋值语句由一个 `name` 名称与一个 `expression` 表达式组成, `=` 绑定表达式运算结果右值到左值 name.

## Doing the assignment
1. 解锁练习 `python3 ok -q test-id -u`
2. 理解问题, 一般 Lab 中会包含函数编写的问题, 首先需要通过 `-u` 解锁问题, 然后完成编写后 再进行测试

### Doctest
```python
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return ______
```

三个双引号包围的行被称作 `docstring`, 它是该函数作用的描述.
`>>>` 开头行被称作 `doctests`, 它会在 Python 解释器运行时被调用, 我们可以在其旁边编写一条表达式, 然后在下面写出预期输出, 如果我们编写函数的实际运行结果与预期输出不同, 则不通过 `doctest`

```shell
python3 ok # 测试所有的练习是否通过
```
# Submitting
在该练习的目录下执行, 进行提交. 由于我们是课外完成, 因此不需要进行提交, 只需在本地判题
```shell
python3 ok --submit
```

```shell
python3 ok --score --local # 本地判题得分
```
```shell
python3 ok --help # 查看 ok 程序帮助
```

```shell
python3 ok -v # 查看当前完成和未完成测试状态
```

# Useful Python command line options
- `python3` 没有参数运行文件, 它会输出结果后返回命令行
- `-i`: 它会运行了我们的 Python 脚本, 然后进入交互模式, 我们可以继续运行代码通过一行行的方式然后得到即时的反馈而不需要把整个文件重新运行一次
- `-m doctest`: 对特定文件的 doctests 运行. `-v` 选项可以查看测试过程 [[doctest)