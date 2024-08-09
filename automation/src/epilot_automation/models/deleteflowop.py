"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_automation.types import BaseModel
from epilot_automation.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteFlowRequestTypedDict(TypedDict):
    flow_id: str
    r"""Automation Workflow ID"""
    

class DeleteFlowRequest(BaseModel):
    flow_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Automation Workflow ID"""
    
