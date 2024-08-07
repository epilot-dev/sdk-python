"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_message.types import BaseModel
from epilot_message.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class MarkReadThreadRequestTypedDict(TypedDict):
    id: str
    r"""Thread ID"""
    

class MarkReadThreadRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Thread ID"""
    
