#!/usr/bin/env python3

"""
this module produce type annotation
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function the type of elemen are not known
    """
    if lst:
        return lst[0]
    else:
        return None
