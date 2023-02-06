#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): value to call wait_random with

    Returns:
        List[float]: list of max_delay seconds
    """
    result = []
    finished = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: finished.append(x.result()))
        result.append(task)

    for task in result:
        await task

    return finished


print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
