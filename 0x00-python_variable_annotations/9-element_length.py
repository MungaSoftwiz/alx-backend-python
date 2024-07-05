#!/usr/bin/env python3
""" Defines module element_length """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return annotaded values """
    return [(i, len(i)) for i in lst]
