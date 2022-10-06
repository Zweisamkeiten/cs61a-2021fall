---
date created: 2022-10-03 15:49
date updated: 2022-10-03 16:01
---

# 解释器

## 解释 Scheme

![](./attachments/Pasted%20image%2020221003155048.png)

## 特殊形式 Special forms

```lisp
(if <predicate> <consequent> <alternative>)
(lambda (<formal-parameters>) <body>)
(define <name> <expression>)
```

特殊形式都由其表达式的第一个元素所确认
其他任何不是特殊形式的组合都需要是一个 Call 调用表达式
![](./attachments/Pasted%20image%2020221003155518.png)

## 逻辑形式 Logical Special forms

逻辑形式 只需要计算其子表达式
![](./attachments/Pasted%20image%2020221003155623.png)
`if` 表达式的值是其子表达式的值

- 计算其条件
- 选择一个子表达式
- 计算子表达式 得到的值为整个表达式的值

## 引述 Quotation

`'<expression>` 是 `(quote <expression>)` 的缩写
`'(1 2)` 等价于 `(quote (1 2))`
其计算结果是返回被引用的表达式而不进行计算

## Frames 帧

![](./attachments/Pasted%20image%2020221003160117.png)

## Lambda 表达式
匿名函数表达式
`(lambda (<formal-parameters>) <body> ...)`
## Define 表达式

`(define <name> <expression>)` 在当前环境的第一个帧中，为表达式绑定到一个名称

过程定义(procedure definition) 是定义一个匿名函数表达式的缩写
`(define (<name> <formal parameters>) <body>)`
`(define <name> (lambda (<formal paramters>) <body>)`

