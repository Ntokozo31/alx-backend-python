#!/usr/bin/env python3

"""
This module contains
asynchronous coroutine
functions for handling
cocurrent delays using the
wait_random function.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    a list of all delays in ascending order.

    Parameters:
        n(int): The number of times to spawn wait_random.
        max_delay: The maximum delay that wait_random can have.

    Return:
        List[float]: A list of float values representing the delays
        returned by wait_random.
    """
    tasks = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]

    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
