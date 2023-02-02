#!/usr/bin/env python3
"""
Defines the function sum_mixed_list
"""
from functools import reduce
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Returns the sum of a list

    Args:
        mxd_lst (List[int, float]): list of numbers

    Returns:
        float: sum of numbers in mxd_lst
    """

    return reduce(lambda x, y: x + y, mxd_lst)
