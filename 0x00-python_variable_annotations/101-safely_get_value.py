#!/usr/bin/env python3
"""
Defines the function safely_get_value
"""
from typing import Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: T | None = None) -> Any | T:
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
