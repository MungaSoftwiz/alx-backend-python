#!/usr/bin/env python
""" Module waits for each other """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Async function that waits for a random delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
