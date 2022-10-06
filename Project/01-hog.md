---
date created: 2022-04-23 13:39
---

# Project: hog

## Phase 1: Simultaor

在每次编写代码解决问题前, 都需要 `python3 ok -q 00 -u` 来解锁相关问题来确保我们已经理解接下来的测试.

### Problem 0

`make_test_dice` 在给定的 dice 列表中循环返回

```python
def make_test_dice(*outcomes):
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
```

`nonlocal` 语句会使得所列出的名称指向之前在最近的包含作用域中绑定的除全局变量以外的变量。[[202204201521]]

这是一个典型的闭包函数用法 [[闭包]], 通过 `nonlocal` 是嵌套函数中的 `index` 指向其外部函数中的 index 所指向的整数对象, 使得 index 成为一个自由变量. 当函数可以从已完成执行的封闭作用域访问局部变量时，就会发生闭包。 dice() 函数调用结束帧栈销毁后, dice 函数对象中的 `index` 依旧指向原指定的整数对象, 因此可以持久化 index 变量.

### Problem 1

> Pig Out rule: 如果掷出的🎲骰子中任一个为 1, 则该当前玩家本轮分数为 1

### Problem 2

> Free Bacon rule:  如果当前玩家选择掷出 0 个 骰子, 则本轮得到 `k + 3` 分.
> k 是取pi小数点后 对手当前分数 位数的数, 特殊情况, 当对手当前分数为 0, 则 `k = 3`, 即 pi 小数点前的数

### Problem 3

`take_turn`, 函数实现了对当前选手选择投掷的骰子个数分支选择是进行 roll_dice, 等于0, 则进行 `free_bacon`.

### Problem 4a

> The Swine Align rule: 当当前玩家完成本轮计分后, 如果两个玩家分数都是整数, 而且两者分数的最大公因数(GCD) 大于等于 10, 则当前玩家可以额外再进行一次投掷

### Problem 4b

> The Pig Pass rule: 当当前玩家完成本轮计分后, 若当前玩家分数小于对手, 且分差小于 3, 则当前玩家可以额外进行一次投掷

### Problem 5

`play` 完成了一个完整的 Hog 游戏, 玩家交替掷骰子, 直到其中一名玩家达到 goαl 分数. `strategy(current_scroe, opponent_score)` 函数会根据两者分数得出本轮掷骰子的个数策略. 其中通过 `while` 循环来判断游戏是否结束, 并根据 `who` 的值来判断本轮当前投掷的玩家, 只有在 `extra_turn` 判断 False, 即结束当前玩家投掷, 才切换到对手玩家.

## Phase 2: Commentray

### Problem 6 7

高阶函数一般使用闭包这种机制来访问自由变量, 高阶函数像是有了状态

```python
def announce_lead_changes(last_leader=None):
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say
```

上述函数中, last_leader 反复根据 say 函数中的条件分支, 选择指向 0, 还是 1. 因此 last_leader 在 say 函数内部已转换为 自由变量. [[Python的高阶函数、自由变量和函数闭包是如何实现的？]] [[闭包]]

## Phase 3: Strategies

### Problem 8

同样是高阶函数相关的知识点

### Problem 9

```shell
python3 hog.py -r
```

**运行实验** 对于本项目的剩余部分，您可以更改 实施 `run_experiments`如你所愿。 通过调用 `average_win_rate`，您可以评估各种 Hog 策略。 例如， 改变第一个 `if False:`到 `if True:`为了评估 `always_roll(8)`反对基线战略 `always_roll(6)`.

一些实验可能需要一分钟才能运行。 你总是可以减少 您调用的试验次数 `make_averaged`以加快实验速度。

### Problem 10

利用 _free_beacon_ 通过滚动 0 这样做是最有益的。 实施 `bacon_strategy`, 返回 0 每当滚动 0 **至少** `cutoff`积分和回报 `num_rolls`除此以外。

### Problem 11

策略也可以利用 _Pig Pass_ 和 _Swine Align_ 规则。 如果这样做会触发额外回合，则额外回合策略总是掷出 0。 在 其他情况下，如果滚动 0 **至少** `cutoff`点。 否则，策略滚动 `num_rolls`.

### 可选：第 12 题（0 分）

实施 `final_strategy`，它结合了这些想法和您的任何其他想法 必须达到高胜率对抗 `always_roll(4)`战略。 一些 建议：

- `extra_turn_strategy`是一个很好的默认策略。
- 得分超过100没有意义。检查您是否可以获胜 滚动 0、1 或 2 个骰子。 如果您处于领先地位，您可能会承担更少的风险。
- 尝试强制额外转弯。
- 选择 `num_rolls`和 `cutoff`仔细论证。
- 采取最有可能赢得比赛的行动。

您可以通过运行 Ok 来检查您的最终策略是否有效。

```shell
python3 ok -q 12
```
