#!/usr/bin/env python3
'''coroutine - measure_runtime'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure the total runtime and return it'''
    start_time = time.perf_counter()
    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
