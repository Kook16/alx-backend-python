#!/usr/bin/env pyython3
'''an async coroutine'''
import asyncio
import random


async def async_generator():
    '''yield a random number between 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)