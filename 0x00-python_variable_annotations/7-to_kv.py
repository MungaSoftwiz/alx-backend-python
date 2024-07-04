#!/usr/bin/env python3
""" Describes a module to_kv """
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of str anf float """
    return (k, v ** 2)
