---
date created: 2022-10-05 10:27
date updated: 2022-10-05 12:04
---

## Backus-Naur Form

BNF 1960 最初用于描述ALGOL language
现在能够描述许多种编程语言

python docs 网页上也用 BNF 语法进行描述

可以用于创建一种语言的解析器

BNF 比 正则更为强大，能够准确匹配一种语言中的括号的匹配性，即使括号是嵌套的

![](./attachments/Pasted%20image%2020221005103309.png)

## BNF syntax

BNF 语法包含一系列语法规则， 可使用 [Lark](https://lark-parser.readthedocs.io/en/latest/) Python package 来使得支持其规则语法。

```BNF
symbol0: symbol1 symbol2 ... symboln
```

标识符中对待字符串有两种

- Non-terminal symbols: 非终结符 可以拓展为其他非终结符或者终结符
- terminal symbols: 终结符 双引号内的字符串，或者常规表达式 由反斜杠包裹

非终结的多个选择 使用 `|`

```BNF
symbol0: symbol1 | symbol2
```

最简语法 三个规则

```BNF
?start: numbers
numbers: INTEGER | numbers "," INTEGER
INTEGER: /-?\d+/
```

在 Lark 库中

- 语法需要由 `start` 标识符开始
- 非终结符的名称必须是小写
- 终结符的名称必须是大写

### 定义终结符

终结符是语法的最基本形式
在 lark 语法中

- 用双引号包裹 eg `"*"`, `"define"`
- 正则表达式由反斜杠包裹 `/` eg `/\d+/`
- 大写标识符由词法规则定义 eg `NUMBER: /\d+(\.\d+/)`

在匹配前忽略终结符，在 Lark 中可以添加 `%ignore`
`%ignore /\s+/      // Ignores all whitespace` 忽略所有的空字符

![](./attachments/Pasted%20image%2020221005110458.png)

## EBNF shorthands

### 重复 repetition

EBNF 是 BNF 的扩展支持一些缩写记号来指定一个特定标识符的匹配的次数
![](./attachments/Pasted%20image%2020221005110610.png)

### 分组

![](./attachments/Pasted%20image%2020221005110914.png)

### Import common terminal 导入通用终结符

Lark 提供预先定义的通用类型数据的终结符

```BNF
%import common.NUMBER
%import common.SIGNED_NUMBER
%import common.DIGIT
%import common.HEXDIGIT
```

![](./attachments/Pasted%20image%2020221005115326.png)

## AST display

```BNF
?start: calc_expr
?calc_expr: NUMBER | calc_op
calc_op: "(" OPERATOR calc_expr* ")"
OPERATOR: "+" | "-" | "*" | "/"
```

- 终结符是叶子节点，不是分叉节点
- Lark 移除没有被命名的符号(例如 `"("` ), 替换命名的终结符 (例如 `OPERATOR`) 或者未命名的常规表达式
- 移除符合由 `?` 开头并且只有一个子节点的规则，替换为他们的子节点 (例如 `calc_expr`)

AST: abstract syntax tree 抽象语法树

## Ambiguity

解决歧义
![](./attachments/Pasted%20image%2020221005120122.png)

改写语法规则
![](./attachments/Pasted%20image%2020221005120158.png)

## BNF IRL

### BNF在哪里使用？

- 语言规范： [Python](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals) ， [CSS](https://www.w3.org/TR/css-values-3/#calc-syntax) , [SaSS](https://github.com/sass/sass/blob/master/spec/syntax.md) [XML](https://www.w3.org/TR/2008/REC-xml-20081126/#sec-logical-struct)
- 文件格式： [谷歌的 robots.txt](https://developers.google.com/search/docs/advanced/robots/robots_txt#formal-syntax-definition)
- 协议： [Apache Kafka](https://kafka.apache.org/0100/protocol.html#protocol_details)
- 解析器和编译器
- 文本生成

![](./attachments/Pasted%20image%2020221005120354.png)
