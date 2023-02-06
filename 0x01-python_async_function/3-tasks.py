#!/usr/bin/env python3
"""
Tasks 3
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Calls wait_random

    Args:
        max_delay (int): value to be passed to wait_random

    Returns:
        asyncio.Task: return value
    """
    return asyncio.create_task(wait_random(max_delay))
