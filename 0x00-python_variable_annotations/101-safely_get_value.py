#!/usr/bin/env python3
"""
Defines the function safely_get_value
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """No idea

    Args:
        dct (Mapping): dictionary
        key (Any): No idea
        default (T | None, optional): Defaults to None.

    Returns:
        Any | T: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
