#### 高阶函数

##### 1. 一些术语和注释

1.  domain，定义域
2.  range，值域
3.  codomain，上域（大概意思应该是：domain是codomain的子集）
4.  文档注释

##### 2. 三条原则

1.  函数应该只做一件明确的事（复杂的文档注释说明函数做得太多）
2.  DRY(Don’t Repeat Yourself)，不要重复，出现重复的代码块建议重构（refactoring），将重复代码块替换成一个单独的函数
3. 定义函数具有普遍性, 例如对不同样式的插头都需要匹配

##### summation举例, 函数作为参数

-   函数是第一类值(first-class values)，可以作为变量传递给函数，也可以作为函数的返回值。求和举例将传入term函数，计算平方和、立方和、级数等。
-   lambda函数

```python
def summation(N, term):
    k = 1
    sum = 0
    while k <= N:
        sum += term(k)
        k += 1
    return sum

def sum_squares(N):
    def square(x):
        return x*x
    return summation(N, square)
# or
def sum_squares(N):
    return summation(N, lambda x: x*x)

def summations():
    print(summation(10, lambda x: x**3))      # Sum of cubes
    print(summation(10, lambda x: 1 / x))     # Harmonic series
    print(summation(10, lambda k: x**(k-1) / factorial(k-1)))  # Approximate e**x
```

#### Functions that return functions, 函数作为返回值

```python
def add_func(f, g):
    """Return function that returns F(x)+G(x) for argument x."""
    def adder(x):           #
        return f(x) + g(x)  # or return lambda x: f(x) + g(x)
    return adder            # 

h = add_func(abs, neg)
print(h(-5))

# Generalizing still more:

def combine_funcs(op):
    def combined(f, g):
        def val(x):
            return op(f(x), g(x))
        return val
    return combined

# Now, can define instead

add_func = combine_funcs(add)

h = add_func(abs, neg)
print(h(-5))
```

-   函数组合在环境中的执行过程  
    ![image](https://img2020.cnblogs.com/blog/2354355/202105/2354355-20210526145622643-2076859231.png)
    
-   这样的条件函数是不存在的  
    ![image](https://img2020.cnblogs.com/blog/2354355/202105/2354355-20210526145840252-1034881847.png)

## Higher-Order Functions 的原因
1. 函数是 first-class: 函数可以被当作值进行操作
2. Higher-order function: 一个函数将一个函数作为参数传入 或者会返回一个函数

作用:
- 表达计算的普遍方法
- 减少程序中重复部分
- 减小函数的耦合度, 就是使两个函数的功能界限更为清晰

## Lambda
![[Pasted image 20220423142021.png]]

## Call Expression
所有参数都先计算为值后应用与函数中