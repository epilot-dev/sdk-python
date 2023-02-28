from __future__ import annotations
import dataclasses
from enum import Enum

class ExecutionStatusEnum(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
