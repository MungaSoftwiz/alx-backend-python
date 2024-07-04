#!/usr/bin/env python3
""" Desfines a module sum-mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums a list of different types """
    return float(sum(mxd_lst))
