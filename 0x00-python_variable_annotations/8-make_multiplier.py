#!/usr/bin/env python3
"""Module takes a float multiplier as argument and returns a function
that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    """
    def func(value: float) -> float:
        return multiplier * value
    return func
