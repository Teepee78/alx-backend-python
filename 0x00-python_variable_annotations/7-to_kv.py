#!/usr/bin/env python3
"""
Defines the function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple

    Args:
        k (str): string
        v (int | float): number

    Returns:
        Tuple[str, float]: k and square of v
    """

    return (k, float(v * v))
