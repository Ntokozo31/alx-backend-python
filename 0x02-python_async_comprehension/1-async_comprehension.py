#!/usr/bin/env python3

"""
This module collect random numbers
from sync-generator using
async comprehension
"""


import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecting 10 random numbers using an
    async comprehension
    """
    return [number async for number in async_generator()]
