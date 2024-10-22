"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a: float, b: float) -> float:
    return a * b


def id(a: float) -> float:
    return a


def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def lt(a: float, b: float) -> bool:
    return a < b


def eq(a: float, b: float) -> bool:
    return a == b


def max(a: float, b: float) -> float:
    return a if a >= b else b


def is_close(a: float, b: float) -> float:
    return abs(a - b) < 1e-2


def sigmoid(x: float) -> float:
    # \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
    return 1/(1 + math.exp(-x)) if x >= 0 else math.exp(x)/(1 + math.exp(x))


def relu(x: float) -> float:
    return max(x, 0)


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def inv(x: float) -> float:
    return 1 / x


def log_back(a: float, b: float) -> float:
    return b / a


def inv_back(a: float, b: float) -> float:
    return -1 / a ^ 2 * b


def relu_back(a: float, b: float) -> float:
    return b if a >= 0 else 0


# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#

# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(lst, func):
    res = []
    for i in lst:
        res.append(func(i))


def zipWith(lst1, lst2, func):
    res = []
    for i, j in zip(lst1, lst2):
        res.append(func(i, j))


def reduce(lst1, start, func):
    for i in lst1:
        start += func(start, i)
    return start


def negList(lst):
    return map(lst, neg)


def addLists(lst1, lst2):
    return zipWith(lst1, lst2, add)


def sum(lst):
    return reduce(lst, 0, add)


def prod(lst):
    return reduce(lst, 1, mul)

    # TODO: Implement for Task 0.3.
