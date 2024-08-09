"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityslug import EntitySlug
from epilot_customer_portal.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class EntityFileCountTypedDict(TypedDict):
    schema_: EntitySlug
    r"""URL-friendly identifier for the entity schema"""
    entity_id: str
    r"""Entity ID"""
    file_count: int
    r"""Number of files associated with the entity and shared with portal user"""
    title: NotRequired[str]
    r"""The title of the parent entity"""
    

class EntityFileCount(BaseModel):
    schema_: Annotated[EntitySlug, pydantic.Field(alias="_schema")]
    r"""URL-friendly identifier for the entity schema"""
    entity_id: str
    r"""Entity ID"""
    file_count: int
    r"""Number of files associated with the entity and shared with portal user"""
    title: Annotated[Optional[str], pydantic.Field(alias="_title")] = None
    r"""The title of the parent entity"""
    
