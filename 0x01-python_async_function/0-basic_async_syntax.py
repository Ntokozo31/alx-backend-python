#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
    max_delay (int): The maximum delay time in seconds. Default is 10.

    Return:
        float: The acual time waited, as float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
