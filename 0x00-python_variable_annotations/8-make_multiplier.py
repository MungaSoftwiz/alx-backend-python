#!/usr/bin/env python3
""" Describes module make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes in a float and returns a function """
    def multiplier_function(param: float) -> float:
        return param * multiplier
    return multiplier_function
