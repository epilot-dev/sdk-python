from __future__ import annotations
import dataclasses
from enum import Enum

class RetryStrategyEnum(str, Enum):
    RETRY_AND_RESUME = "RETRY_AND_RESUME"
    RETRY_AND_STOP = "RETRY_AND_STOP"
