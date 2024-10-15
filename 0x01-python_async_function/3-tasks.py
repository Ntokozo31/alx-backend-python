#!/usr/bin/env python3

"This module provide a function that returns asyncio.Task"

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    "Normal function that returns asyncio.Task"

    task = asyncio.create_task(wait_random(max_delay))

    return task
