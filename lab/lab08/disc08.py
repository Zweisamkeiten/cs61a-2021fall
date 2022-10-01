class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print("boo!")
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret


class Link:
    """A linked list."""

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


# Q3: Sum Nums


def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if not s:
        return 0
    return s.first + sum_nums(s.rest)


# Q4: Multiply Links
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        product *= link.first
    lst_of_lnks = [link.rest for link in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks))


# Q5: Filp Two
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if not s or not s.rest:
        return
    temp = s.first
    s.first = s.rest.first
    s.rest.first = temp
    flip_two(s.rest.rest)


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


# Q6: Make even
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    if t.is_leaf():
        return
    for b in t.branches:
        make_even(b)


# Q7: Leaves
def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    if t.is_leaf():
        return [t.label]
    result = []
    for b in t.branches:
        result += leaves(b)
    return result


# Q8: Find Paths
# def find_path(t, x):
#     """
#     >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])] ), Tree(15)])
#     >>> find_path(t, 5)
#     [2, 7, 6, 5]
#     >>> find_path(t, 10) # returns None"""
#     if t.label == x:
#         return [t.label]
#     for b in t.branches:
#         path = find_path(b, x)
#         if path:
#             return [t.label] + path
def find_paths(t, entry):
    """
    >>> t1 = Tree(2)
    >>> find_paths(t1, 1)
    []
    >>> find_paths(t1, 2)
    [[2]]
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths
