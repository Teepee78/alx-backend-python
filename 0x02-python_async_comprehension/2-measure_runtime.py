#!/usr/bin/env python3
"""
Defines measure_runtime coroutine
"""
import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of 4 async_comprehensions

    Returns:
        float: total runtime
    """
    start = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time() - start
