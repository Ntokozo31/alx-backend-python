#!/usr/bin/env python3

"""
This module produce type annotation
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence]]:
    """
    Function returns list as tuples
    """
    return [(i, len(i)) for i in lst]
