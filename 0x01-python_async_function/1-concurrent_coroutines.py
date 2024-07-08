#!/usr/bin/env python3
"""Multiple coroutines at the same time with async """
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    async routine called wait_n that takes in 2 int arguments
    n and max_delay and returns the list of all the delays (float values)
    in ascending order without using sort().
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
