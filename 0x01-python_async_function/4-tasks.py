#!/usr/bin/env python3
"""
Tasks 4
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        task = task_wait_random(max_delay - 1)
        task.add_done_callback(lambda x: finished.append(x.result()))
        tasks.append(task)

    for task in tasks:
        await task

    return finished


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
