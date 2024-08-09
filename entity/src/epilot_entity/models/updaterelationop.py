"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_entity.types import BaseModel
from epilot_entity.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateRelationRequestBodyTypedDict(TypedDict):
    tags: NotRequired[List[str]]
    

class UpdateRelationRequestBody(BaseModel):
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    

class UpdateRelationRequestTypedDict(TypedDict):
    attribute: str
    r"""The attribute that express meaning"""
    entity_id: str
    r"""The attribute that express meaning"""
    id: str
    r"""Entity id"""
    slug: str
    r"""Entity Type"""
    request_body: NotRequired[UpdateRelationRequestBodyTypedDict]
    activity_id: NotRequired[str]
    r"""Activity to include in event feed"""
    async_: NotRequired[bool]
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    

class UpdateRelationRequest(BaseModel):
    attribute: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The attribute that express meaning"""
    entity_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The attribute that express meaning"""
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity id"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity Type"""
    request_body: Annotated[Optional[UpdateRelationRequestBody], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    activity_id: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Activity to include in event feed"""
    async_: Annotated[Optional[bool], pydantic.Field(alias="async"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = False
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    
