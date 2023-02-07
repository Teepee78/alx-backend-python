#!/usr/bin/env python3
"""
Defines measure_runtime coroutine
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of 4 async_comprehensions

    Returns:
        float: total runtime
    """
    start = time.time()

    # await asyncio.gather(
    #     async_comprehension(),
    #     async_comprehension(),
    #     async_comprehension(),
    #     async_comprehension()
    # )
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    return time.time() - start
