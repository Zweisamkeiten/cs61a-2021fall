from pair import Pair, nil

# Q1
# (+ (- 2 4) 6 8)
# Pair("+", Pair(Pair("-", Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))
# "+" "-"
# p.first p.rest.first.first
# 2 4 6 8
# p.rest.first.rest.first p.rest.first.rest.rest.first p.rest.rest.first p.rest.rest.rest.first
#

# Q2
OPERATORS = ["//"]


def calc_eval(exp):
    if isinstance(exp, Pair):  # Call expressions
        return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:  # Names
        return OPERATORS[exp]
    else:  # Numbers
        return exp


def floor_div(expr):
    if expr.rest == nil:
        return expr.first
    expr.rest.first = calc_eval(expr.first) // calc_eval(expr.rest.first)


# Assume OPERATORS['//'] = floor_div is added for you in the code

# Q3
#  Are we able to handle expressions containing the comparison operators (such as <, >, or =) with the existing implementation of calc_eval? Why or why not?
# Comparison expressions are regular call expressions, so we need to evaluate the
# operator and operands and then apply a function to the arguments. Therefore,
# we do not need to change calc eval. We simply need to add new entries to the
# OPERATORS dictionary that map ’<’, ’>’, and ’=’ to functions that perform the
# appropriate comparison operation.
# 组合表达式是常规调用表达式，可以直接使用原有的 calc_eval

# Are we able to handle and expressions with the existing implementation of calc_eval? Why or why not?
# Since and is a special form that short circuits on the first false-y operand,
# we cannot handle these expressions the same way we handle call expressions.
# We need to add special handling for combinations that don’t evaluate all the
# operands.
# and 表达式是是特殊形式，它是短路的。因此需要修改 calc_eval


def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == "and":  # and expressions
            return eval_and(exp.rest)
        else:  # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:  # Names
        return OPERATORS[exp]
    else:  # Numbers
        return exp


def eval_and(operands):
    curr, val = operands, True
    while curr is not nil:
        val = calc_eval(curr.first)
        if val is False:
            return False
        curr = curr.rest
    return val


# Q4
bindings = {}


def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == "and":  # and expressions[paste your answer from the earlier]
            return eval_and(exp.rest)
        elif exp.first == "define":  # define expressions
            return eval_define(exp.rest)

        else:  # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif bindings.get(exp.first):  # Looking up variables
        return bindings.get(exp.first)
    elif exp in OPERATORS:  # Looking up procedures
        return OPERATORS[exp]
    else:  # Numbers
        return exp


def eval_define(expr):
    bindings[expr.first] = calc_eval(expr.rest)


# Q5
# How many calls to calc_eval and calc_apply would it take to evaluate each of the following Calculator expressions?

# scm> (+ 1 2)
# 4 calls to eval: 1 for the entire expression, and then 1 each for the operator and each operand
# 1 call to apply the addition operator.

# scm> (+ 2 4 6 8)
# 6 calls to eval: 1 for the entire expression, and then 1 each for the operator and each operand
# 1 call to apply the addition operator.

# scm> (+ 2 (* 4 (- 6 8)))
# 10 calls to eval: 1 for the whole expression, and then 1 each for the sub expression. and 1 each for the operator and each operand.
# 3 calls to apply the funciton to the arguments for each call expression.

# scm> (and 1 (+ 1 0) 0)
# 11 calls to eval: 1 for the whole expression, and then 1 for the operator and each operand, and for short-circuit and 3 calls, and 1 call for sub expression
# 1 call to apply the addition operator.

#  Q6
Pair("+", Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
