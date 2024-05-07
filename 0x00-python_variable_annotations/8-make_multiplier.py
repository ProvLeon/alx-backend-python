#!/usr/bin/env python3
"""
Defining a function that returns takes a float
and returns a function that multiplies a float
by a multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float.
    """
    return lambda x: x * multiplier
