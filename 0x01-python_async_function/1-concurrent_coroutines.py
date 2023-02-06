#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawns wait_random n times

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): value to call wait_random with

    Returns:
        List[float]: list of max_delay seconds
    """
    tasks = []
    finished = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay - 1))
        task.add_done_callback(lambda x: finished.append(x.result()))
        tasks.append(task)

    for task in tasks:
        await task

    return finished
