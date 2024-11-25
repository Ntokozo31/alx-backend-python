#!/usr/bin/env python3


"""
This module produce type annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum function of mixed numbers
    """
    return sum(mxd_lst)
