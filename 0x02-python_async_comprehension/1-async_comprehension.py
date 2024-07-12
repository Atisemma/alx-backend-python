#!/usr/bin/env python3
"""Module for the async_comprehension coroutine."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [num async for num in async_generator()]
