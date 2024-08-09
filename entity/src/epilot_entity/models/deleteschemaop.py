"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_entity.types import BaseModel
from epilot_entity.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteSchemaRequestTypedDict(TypedDict):
    slug: str
    r"""Entity Type"""
    

class DeleteSchemaRequest(BaseModel):
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity Type"""
    
