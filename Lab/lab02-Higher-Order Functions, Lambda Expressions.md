## Lambda Expressions

Lambda expressions are expressions that evaluate to functions by specifying two things: the parameters and a return expression.

```
lambda <parameters>: <return expression>
```

While both `lambda` expressions and `def` statements create function objects, there are some notable differences. `lambda` expressions work like other expressions; much like a mathematical expression just evaluates to a number and does not alter the current environment, a `lambda` expression evaluates to a function without changing the current environment. Let's take a closer look.

|--|lambda|def|
|--|--|--|
|Type|_Expression_ that evaluates to a value|_Statement_ that alters the environment|
|Result of execution|Creates an anonymous lambda function with no intrinsic name.|Creates a function with an intrinsic name and binds it to that name in the current environment.|
|Effect on the environment|Evaluating a `lambda` expression does _not_ create or modify any variables.|Executing a `def` statement both creates a new function object _and_ binds it to a name in the current environment.|
|用法|一个 `lambda`表达式可以在任何地方使用 需要一个表达式，例如在赋值语句中或作为 调用表达式的运算符或操作数。|执行后 `def`声明，创建 函数绑定到一个名称。 您应该使用此名称来指代 在任何需要表达式的地方起作用。|

```python
# A lambda expression by itself does not alter
# the environment
lambda x: x * x

# We can assign lambda functions to a name
# with an assignment statement
square = lambda x: x * x
square(3)

# Lambda expressions can be used as an operator
# or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)
```
```python
def square(x):
    return x * x

# A function created by a def statement
# can be referred to by its intrinsic name
square(3)
```

## 环境图

环境图是理解的最佳学习工具之一 `lambda`表达式和高阶函数，因为你可以保持 跟踪所有不同的名称、函数对象和函数的参数。 我们强烈建议绘制环境图或使用 [Python 。](https://tutor.cs61a.org) 

### 赋值语句

1.  计算右边的表达式 `=`符号。
2.  如果在左侧找到的名称 `=`不存在于 当前帧，将其写入。如果是，则删除当前绑定。 绑定 _值_ 到此名称。

如果语句中有多个名称/表达式，则评估所有 在进行任何绑定之前，表达式首先从左到右。

### def 语句

1.  绘制函数对象及其内在名称、形式参数和 父 frame。 函数的父框架是函数所在的框架 定义。
2.  如果当前函数中不存在函数的固有名称 frame，将其写入。如果是，则删除当前绑定。 绑定新的 为此名称创建了函数对象。

### 调用表达式

> 注意：对于像这样的内置 Python 函数，您不必经历此过程 `max`或者 `print`.

1.  评估运算符，其值应该是一个函数。
2.  从左到右计算操作数。
3.  打开一个新框架。 用顺序帧号标记它，内在的 函数的名称及其父级。
4.  将函数的形式参数绑定到您的值的参数 在步骤 2 中找到。
5.  在新环境中执行函数体。

### lambda

> _注意：_ 正如我们在 `lambda`上面的表达部分， `lambda`函数没有内在名称。 画画的时候 `lambda`中的功能 环境图，它们标有名称 `lambda`或与 小写希腊字母 λ。 当有 环境图中的多个 lambda 函数，因此您可以区分 给它们编号或写下定义它们的行号。

1.  绘制 lambda 函数对象并用 λ 标记它，它的形式 参数及其父框架。 函数的父框架是 定义了哪个函数。

这是唯一的一步。 我们包括这一部分是为了强调一个事实 和...之间的不同 `lambda`表达式和 `def`陈述是 `lambda`表达式 _不会_ 在环境中创建任何新绑定。