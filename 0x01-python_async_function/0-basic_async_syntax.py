#!/usr/bin/env python3
"""
Basic async syntax in python
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds between 0 and max_delay

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        (float): The number of seconds funtion delayed for
    """
    num = uniform(0, max_delay + 1)
    await asyncio.sleep(num)
    return num
