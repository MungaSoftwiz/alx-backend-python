#!/usr/bin/env python3
""" Defines sum_list module """
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns sum of input_list as floats """
    return reduce(lambda x, y: x + y, input_list)
