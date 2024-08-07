"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_workflows_execution.types import BaseModel
from epilot_workflows_execution.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetClosingReasonExecutionRequestTypedDict(TypedDict):
    execution_id: str
    r"""Id of the execution"""
    

class GetClosingReasonExecutionRequest(BaseModel):
    execution_id: Annotated[str, pydantic.Field(alias="executionId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Id of the execution"""
    
