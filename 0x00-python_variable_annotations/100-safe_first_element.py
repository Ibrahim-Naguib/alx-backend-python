#!/usr/bin/env python3
"""Module uses duck-typed annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves the first element from a list safely."""
    if lst:
        return lst[0]
    else:
        return None
