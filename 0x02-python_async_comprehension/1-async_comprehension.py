#!/usr/bin/env python3
"""
Defines a coroutine async_comprehension
"""
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Iterates over an async generator

    Returns:
        List[float]: list of floats
    """
    return [num async for num in async_generator()]
