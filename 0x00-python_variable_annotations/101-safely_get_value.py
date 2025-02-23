#!/usr/bin/env python3
"""Module uses duck-typed annotations"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieves a value from a dictionary safely.
    """
    if key in dct:
        return dct[key]
    else:
        return default
