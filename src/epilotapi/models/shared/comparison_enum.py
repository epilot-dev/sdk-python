import dataclasses
from enum import Enum

class ComparisonEnum(str, Enum):
    EQUALS = "equals"
    ANY_OF = "any_of"
    NOT_EMPTY = "not_empty"
    IS_EMPTY = "is_empty"
