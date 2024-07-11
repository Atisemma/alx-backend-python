#!/usr/bin/env python3
"""Module for zooming arrays using type annotations."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of a tuple.

    Args:
        lst (Tuple): The input tuple to zoom.
        factor (int): The zoom factor. Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
