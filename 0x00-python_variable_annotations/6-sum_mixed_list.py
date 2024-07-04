#!/usr/bin/env python3
'''A type-annotated function to sum a list of mixed types.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a list containing integers and floats as a float.'''
    return float(sum(mxd_lst))
