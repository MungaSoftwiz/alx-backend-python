#!/usr/bin/env python3
""" Define safely_get_value module"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Add type annotations to function"""

    if key in dct:
        return dct[key]
    else:
        return default
