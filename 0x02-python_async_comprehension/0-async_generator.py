#!/usr/bin/env python3

"This module proveide the function that generate random number"

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutin will loop 10 times each time async wait 1 second
    then yield a random number from 0 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
