#!/usr/bin/env python3
""" Validate code with mypy """
from typing import Any, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Type annotate where necessary """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
