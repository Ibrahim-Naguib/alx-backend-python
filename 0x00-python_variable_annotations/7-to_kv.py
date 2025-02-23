#!/usr/bin/env python3
"""Module takes a string k and an int OR float v and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv that takes a string k and an int OR float v
    as arguments and returns a tuple
    """
    return (k, v ** 2)
