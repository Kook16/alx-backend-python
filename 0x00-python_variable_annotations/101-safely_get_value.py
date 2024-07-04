#!/usr/bin/env python3
'''function'''
from typing import Sequence, Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None]
) -> Union[Any, T]:
    '''....'''
    if key in dct:
        return dct[key]
    else:
        return default
