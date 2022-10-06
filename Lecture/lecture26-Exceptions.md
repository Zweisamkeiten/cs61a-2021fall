---
date created: 2022-10-03 09:18
date updated: 2022-10-03 09:43
---

# Exceptions

## Scheme: programs as data

表示数据结构的方法:

```lisp
(list 'quotient 10 2) ; (quotient 10 2)
(eval (list 'quotient 10 2)) ; 5
```

### Quasiquotation 解引用

- Quote: `'(a b)` => `(a b)`
- Quasiquote:  ``(a b)`    =>  `(a b)`

Different ` 可以被解引用

```lisp
(define b 4)

'(a ,(+ b 1)) =>  (a (unquote (+ b 1)))
`(a , (+ b 1)) =>  (a 5)
```

```lisp
(define (make-adder n) `(lambda (d) (+ d, n)))
(make-adder 2) ; (lambda (d) (+ d 2))
```

## Python: Exceptions

当程序以预期外的方式运行

- 函数接受到不正确类型的参数值

- 某些资源（例如文件）不可用

- 数据传输过程中网络连接丢失

- **exception** 异常是编程语言中用于声明和响应异常的内置机制条件

- 发生错误时， 程序会引发异常

- 如果不处理异常，程序将完全停止运行

- 程序中增加处理异常的代码，以便程序继续运行

### 异常类型

- **OverflowError** ex: `pow(2.12, 10000)` 溢出
- **TypeError** ex: `'hello'[1] = 'j'` 类型错误
- **IndexError** ex: `'hello'[7]` 下标越界
- **NameError** ex: `x += 5` x is not defined 名称错误
- **FileNotFoundError** ex: `open('dsfdfd.txt')` 文件不存在

完整列表 [请参阅例外文档](https://docs.python.org/3/library/exceptions.html) 。

### Try 语句处理异常

```python
try:
	<try suite>
except <exception class> as <name>:
	<except suite>
```

`<try suite>` 首先执行，如果执行过程中引发了一个不以其他方式处理的异常，且异常类继承自 `<exception class>`, 将异常绑定到 `<name>`,  执行 `<exception suite>`.

```python
try:
    quot = 10/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    quot = 0
```

### 引发异常 Raising exceptions

**AssertionError** type exception
`assert <expression>, <string>`

断言默认设置为自由使用，可以使用 "-O" 标志运行Ptyhon 忽略它们以提高
效率

`python3 -O`

产生其他类型的异常
`raise <expression>`
`<expression>` 必须评估为 `BaseException`或一个实例
异常的构造与任何其他对象一样。 例如， `TypeError('Bad argument!')`
