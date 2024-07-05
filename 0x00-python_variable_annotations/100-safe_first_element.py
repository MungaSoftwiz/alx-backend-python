#!/usr/bin/env python3
""" Defines module safe_first_element"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns first arg or none"""
    if lst:
        return lst[0]
    else:
        return None
