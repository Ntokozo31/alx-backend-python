#!/usr/bin/env python 3

"""
This module contains
asynchronous coroutine
functions for handling
cocurrent delays using the
wait_random function.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random #import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
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
    tasks = [] #Initialize an empty list to host tasks

    #Loop n times to creat and gather tasks
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay)) #Creat an asyncio task
        tasks.append(task) #Add task to the list of tasks

    delays = await asyncio.gather(*tasks) #Wait for all tasks to complete and gather result

    return delays #Return the list of delays
