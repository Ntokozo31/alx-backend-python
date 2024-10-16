#!/usr/bin/env python3

"""
This module collect random numbers
from sync-generator using
async comprehension
"""
import asyncio
from typing import AsyncGenerator
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    Collecting 10 random numbers using an
    async comprehension
    """
    async for number in async_generator():
        yield number
