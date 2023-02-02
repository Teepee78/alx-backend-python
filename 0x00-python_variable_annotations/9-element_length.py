#!/usr/bin/env python3
"""
Defines the element_length function
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """No idea

    Args:
        lst (Iterable[Sequence]): Iterable

    Returns:
        List[Tuple[Sequence, int]]: List
    """

    return [(i, len(i)) for i in lst]
