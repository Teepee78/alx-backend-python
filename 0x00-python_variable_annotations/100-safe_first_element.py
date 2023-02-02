#!/usr/bin/env python3
"""
Defines the safe_first_element function
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """No idea

    Args:
        lst (Sequence[Any]): Sequence of elements

    Returns:
        Any | None: Any
    """

    if lst:
        return lst[0]
    else:
        return None
