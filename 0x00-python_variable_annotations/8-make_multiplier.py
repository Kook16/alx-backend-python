#!/usr/bin/env python3
'''type-annotated function make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies its input by the given multiplier.'''
    def multipler_func(val: float) -> float:
        return val * multiplier
    return multipler_func
