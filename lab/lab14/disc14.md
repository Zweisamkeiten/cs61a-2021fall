理解就是一切

（改编自 2021 年春季决赛） 下面的 EBNF 文法可以描述 Python 列表推导，但还不能描述所有这些。

start: comp

?comp: "[" expression "for" IDENTIFIER "in" IDENTIFIER "]"

expression: IDENTIFIER operation*

operation: OPERATOR NUMBER

IDENTIFIER: /[a-zA-Z]+/

OPERATOR: "*" | "/" | "+" | "-"

%import common.NUMBER
%ignore /\s+/

选择语法中的所有非终结符号：

    - comp
    - expression
    - operation
    - NUMBER
    - IDENTIFIER
    - OPERATOR

你的答案：

    - comp
    - expression
    - operation

下列哪些推导会被语法成功解析？

    - [ x * 2 for x in list ]
    - [ x for x in list ]
    - [ x ** 2 for x in list ]
    - [ x + 2 for x in list if x == 1 ]
    - [ x * y for x in list for y in list2 ]
    - [ x - 2 for x in my_list ]
    - [ x - y for (x,y) in tuples ]

你的答案：

    - [ x * 2 for x in list ]
    - [ x for x in list ]

我们需要修改哪一行来支持 `%`， 就像在表达 [ n % 2 for n in numbers ]?

    - OPERATOR: "*" | "/" | "+" | "-"
    - IDENTIFIER: /[a-zA-z]+/
    - operation: OPERATOR NUMBER
    - expression: IDENTIFIER operation*
    - ?comp: "[" expression "for" IDENTIFIER "in" IDENTIFIER "]"

答案:
    - OPERATOR: "*" | "/" | "+" | "-" | "%"


