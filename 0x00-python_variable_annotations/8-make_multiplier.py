#!/usr/bin/env python3
"""
Defines the function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a function by a multiplier

    Args:
        multiplier (float): multiplier

    Returns:
        function: multiplier function
    """

    return lambda x: x * multiplier
