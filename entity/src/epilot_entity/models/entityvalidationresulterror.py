"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityvalidationerror import EntityValidationError
from enum import Enum
from epilot_entity import utils
from epilot_entity.types import BaseModel
from typing import List


class SchemasStatus(str, Enum):
    ERROR = "error"
class EntityValidationResultErrorData(BaseModel):
    errors: List[EntityValidationError]
    status: SchemasStatus
    


class EntityValidationResultError(Exception):
    r"""Validation result for a failed validation"""
    data: EntityValidationResultErrorData

    def __init__(self, data: EntityValidationResultErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, EntityValidationResultErrorData)

