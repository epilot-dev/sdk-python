import dataclasses
from enum import Enum

class MappingAttributeModeEnum(str, Enum):
    COPY_IF_EXISTS = "copy_if_exists"
    APPEND_IF_EXISTS = "append_if_exists"
    SET_VALUE = "set_value"

