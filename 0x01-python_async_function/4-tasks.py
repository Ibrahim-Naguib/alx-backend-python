#!/usr/bin/env python3
"""Returning a Task"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that takes an integer max_delay and returns a asyncio.Task
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = asyncio.gather(*tasks)
    return [await task for task in asyncio.as_completed(tasks)]
