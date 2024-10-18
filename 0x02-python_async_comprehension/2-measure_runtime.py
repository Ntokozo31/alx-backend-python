#!/usr/bin/env python3

"""
This module will execute async_comprehension four
times in parallel
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that execute async_comprehension four
    times in parallel using asyncio.gather
    """
    start_time = asyncio.get_running_loop().time()

    task = [
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension())
            ]
    await asyncio.gather(*task)
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
