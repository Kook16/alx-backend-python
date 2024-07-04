#!/usr/bin/env python3
'''type-annotated function to_kv'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Rets tuple the first ele is a str and the 2nd is the sq of the num.'''
    return (k, v ** 2)
