"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .relationitem import RelationItem, RelationItemTypedDict
from epilot_entity.types import BaseModel
from epilot_entity.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RemoveRelationsRequestTypedDict(TypedDict):
    id: str
    r"""Entity id"""
    slug: str
    r"""Entity Type"""
    request_body: NotRequired[List[RelationItemTypedDict]]
    async_: NotRequired[bool]
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    

class RemoveRelationsRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity id"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity Type"""
    request_body: Annotated[Optional[List[RelationItem]], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    async_: Annotated[Optional[bool], pydantic.Field(alias="async"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = False
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    
