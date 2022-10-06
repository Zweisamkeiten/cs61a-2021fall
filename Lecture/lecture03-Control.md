### Lecture #3: Recap of Function Evaluation; Control

重述一下Function Evaluation；Control 流程控制 （Ch1.5）

#### recap

-   总结environment的特点。
-   举例讲解environment chain，evaluation of a call，composingprograms网站有接入pythontutor可以一步步execute。  
    ![image](https://img2020.cnblogs.com/blog/2354355/202105/2354355-20210525112733560-1823672857.png)

1.  p9 id(x)函数部分，尝试将`return x` 改为`return 2*x` 报错：int和function类型不能进行运算，不传入id函数作为参数`print(id(id(13)))`可得到结果52。
2.  嵌套函数调用的environment情况，包括global frame 和local frame。

#### control
[[lab01-Variables-Functions-Control#布尔运算符 bool]]
conditional expressions 条件表达式  
`TruePart if Condition else FalsePart`

##### 1. "true value"

false value 包括:

-   false
-   None
-   0
-   Empty strings, sets, lists, tuples, and dictionaries

##### 2. short-circuit evaluation

left **and** right 和 left **or** right 的短路特性  
![image](https://img2020.cnblogs.com/blog/2354355/202105/2354355-20210525151023286-304981078.png)

-   **left and right**：先计算left，如果left为false，表达式的值为left，不计算right的值（不判断right是否有意义，如1/0）；否则，表达式值为right。
-   **left or right**： 先计算left，如果left为true，表达式的值为left，不计算right的值（不判断right是否有意义，如1/0）；否则，表达式值为right。

##### 3. conditional statement 条件语句
[[lab01-Variables-Functions-Control#If statements]]
```yaml
if Condition1:
  Statements1
elif Condition2:
  Statements2
...
else:
  Statementsn
```

###### 4. alternative definition

```kotlin
def signum(x):
  if x > 0:
    return 1
  elif x == 0:
    return 0
  else:
    return -1
```

等效于

```java
def signum(x):
  return 1 if x > 0 else 0 if x == 0 else -1
```

##### 5. iteration

-   suites and sequences，缩进语句的序列是一个suite
-   iteration，recursion function会在后续课程中讲解
-   while statement，循环语句
-   理解：同样的迭代计算，在[pythontutor](http://pythontutor.com/composingprograms.html "pythontutor")中尝试，recursion方法会使用n个local frame，while方法只在global frame中做substitution

```perl
# Iteration via recursion (preview) 
def add_sq(accum, k, n):
    """Return ACCUM + K ** 2 + (K+1)**2 + ... + N**2."""
    if k > n:
        return accum
    else:
        return add_sq(accum + k ** 2, k + 1, n)
print(add_sq(0, 1, 100))

# Iteration via while loop (indefinite repetition)
accum = 0
k = 1
n = 100
while k <= n:
    accum = accum + k ** 2
    k += 1    # Another way to write k = k + 1
print(accum)
```