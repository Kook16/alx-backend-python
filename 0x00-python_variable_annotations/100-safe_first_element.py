#!/usr/bin/env python3
'''functions'''
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''add type annotations to the function'''
    if lst:
        return lst[0]
    else:
        return None
