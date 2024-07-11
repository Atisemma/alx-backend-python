#!/usr/bin/env python3
"""Module for safely getting a value from a dictionary."""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.
    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up.
        default (Union[T, None], optional): Default value. Defaults to None.
    Returns:
        Union[Any, T]: Value if key exists, else default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
