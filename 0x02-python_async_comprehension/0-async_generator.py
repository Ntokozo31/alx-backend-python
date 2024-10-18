#!/usr/bin/env python3

"""
This module proveide the
Async Generator
"""

import asyncio
import random


async def async_generator():
    """
    Coroutin will loop 10 times each time async wait 1 second
    then yield a random number from 0 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
