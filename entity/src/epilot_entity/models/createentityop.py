"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entity_input import EntityInput, EntityInputTypedDict
from epilot_entity.types import BaseModel
from epilot_entity.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateEntityRequestTypedDict(TypedDict):
    slug: str
    r"""Entity Type"""
    entity: NotRequired[EntityInputTypedDict]
    activity_id: NotRequired[str]
    r"""Activity to include in event feed"""
    async_: NotRequired[bool]
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    

class CreateEntityRequest(BaseModel):
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Entity Type"""
    entity: Annotated[Optional[EntityInput], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    activity_id: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Activity to include in event feed"""
    async_: Annotated[Optional[bool], pydantic.Field(alias="async"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = False
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    
