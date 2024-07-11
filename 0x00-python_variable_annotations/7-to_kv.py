#!/usr/bin/env python3
"""Module for creating a tuple from a string and a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): String for the first tuple element.
        v (Union[int, float]): Number to be squared.

    Returns:
        Tuple[str, float]: Tuple of string and squared number.
    """
    return (k, float(v ** 2))
