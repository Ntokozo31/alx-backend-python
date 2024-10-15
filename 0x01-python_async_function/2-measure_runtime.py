#!/usr/bin/ env python3

"""
This module provide a function to measure the runtime of the wait_n
function from the 1_concurrent_coroutine module.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n #import 1_concurrent_coroutine

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for the wait_n function
    and return the avarage time per call.

    Parameters:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay to be used in wait_n.

    Return:
        float: The avarage execution time for the wait_n function
        in seconds.
    """

    start_time = time.time() #Record the start time

    asyncio.run(wait_n(n, max_delay)) #Run wait_n asynchronously

    total_time = time.time() - start_time #Calculate the elapsed time

    return total_time / n #Return the avarage time per call
