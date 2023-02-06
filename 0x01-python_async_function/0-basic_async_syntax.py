#!/usr/bin/env python3
"""
Basic async syntax
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> int:
    """Waits for a random number of seconds between 0 and max_delay

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        The number of seconds funtion delayed for
    """
    num = uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
