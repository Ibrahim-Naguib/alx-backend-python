#!/usr/bin/env python3
"""Module return values with the appropriate types"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
