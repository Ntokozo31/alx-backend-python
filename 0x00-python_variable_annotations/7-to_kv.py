#!/usr/bin/env python3


"""
This module produce type annotation
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function the frist return element is a string
    second is a square
    """
    return (k, v ** 2)
