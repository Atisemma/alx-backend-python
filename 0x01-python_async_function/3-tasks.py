#!/usr/bin/env python3
"""Module for creating an asyncio.Task from wait_random."""

import asyncio
from typing import Union

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: A Task that will execute wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
