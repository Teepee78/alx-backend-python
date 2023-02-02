#!/usr/bin/env python3
"""
Defines the sum_list function
"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats

    Args:
        input_list (List[float]): List of floats

    Returns:
        float: sum of input_list
    """

    return reduce(lambda x, y: x + y, input_list)
