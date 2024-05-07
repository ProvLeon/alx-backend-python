#!/usr/bin/env python3
"""
Defining an input list with
mixed types with annotations
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns list of floats or int
    """
    return sum(mxd_list)
