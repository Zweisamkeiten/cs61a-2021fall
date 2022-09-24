# Environments

- 每一个用户定义的函数有一个父 frame, 帧(通常为 Global)
- 一个函数的父函数是其在被定义的frame
- 每一个本地frame有一个父frame(通常为Global)
- 一个 frame 的父frame 是其调用函数的父函数

![](./attachments/Pasted%20image%2020220423164148.png)

当一个函数中的局部变量被子作用域视为自由变量时，就代表这个变量的生命周期可能会超过定义它的函数的生命周期。在第二趟的检查的回溯阶段，这些符号会从局部变量中移除，添加到 ![公式](https://www.zhihu.com/equation?tex=%5Ctexttt%7Bcellvars%7D) 集合中。除此以外，CPython要求在后续生成代码时，定义这些变量的函数要用cell将它们打包起来（类似于Java的packed type），这样才能保证函数执行后这些变量不会被销毁。
![](./attachments/Pasted%20image%2020220423170019.png)
因为pytutor 会显示已经销毁exited functions的frames, 实际上应该解释为上述的 cell 的生命周期.

![](./attachments/Pasted%20image%2020220423165257.png)

某次函数调用的 父frame 是其在被定义的位置 frame


## Currying:
Currying: 是将一个多参数的函数转换为一次接收一个参数的高阶函数

```python
def make_adder(n):
	return lambda k: n + k

make_adder(2)(3) === add(2, 3) == (lambda n: lambda k: n + k)(2)(3)
```

