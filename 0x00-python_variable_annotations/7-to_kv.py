#!/usr/bin/env python3
"""
Defining a function that takes in a str
and int/float and returns a tuple
of str and float with type annotations
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple.
    """
    return (k, v**2)
