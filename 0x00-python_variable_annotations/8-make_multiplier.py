#!/usr/bin/env python3
"""Module providing a function to create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        A function that takes a float and returns a float.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
