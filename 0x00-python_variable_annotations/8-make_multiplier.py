#!/usr/bin/env python3

"""
This module produce type annotation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies a float by multiplier
    """
    def multiplier_function(value: float) -> float:
        """
        Function that multies value by multiplier
        """
        return value * multiplier
    return multiplier_function
