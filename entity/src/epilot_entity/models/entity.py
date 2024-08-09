"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityacl import EntityACL, EntityACLTypedDict
from .entityowner import EntityOwner, EntityOwnerTypedDict
from datetime import datetime
from epilot_entity.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import ConfigDict, model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class EntityTypedDict(TypedDict):
    acl: NotRequired[EntityACLTypedDict]
    r"""Access control list (ACL) for an entity. Defines sharing access to external orgs or users."""
    created_at: NotRequired[Nullable[datetime]]
    id: NotRequired[str]
    org: NotRequired[str]
    r"""Organization Id the entity belongs to"""
    owners: NotRequired[List[EntityOwnerTypedDict]]
    schema_: NotRequired[str]
    r"""URL-friendly identifier for the entity schema"""
    tags: NotRequired[Nullable[List[str]]]
    title: NotRequired[Nullable[str]]
    r"""Title of entity"""
    updated_at: NotRequired[Nullable[datetime]]
    

class Entity(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    acl: Annotated[Optional[EntityACL], pydantic.Field(alias="_acl")] = None
    r"""Access control list (ACL) for an entity. Defines sharing access to external orgs or users."""
    created_at: Annotated[OptionalNullable[datetime], pydantic.Field(alias="_created_at")] = UNSET
    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    org: Annotated[Optional[str], pydantic.Field(alias="_org")] = None
    r"""Organization Id the entity belongs to"""
    owners: Annotated[Optional[List[EntityOwner]], pydantic.Field(alias="_owners")] = None
    schema_: Annotated[Optional[str], pydantic.Field(alias="_schema")] = None
    r"""URL-friendly identifier for the entity schema"""
    tags: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="_tags")] = UNSET
    title: Annotated[OptionalNullable[str], pydantic.Field(alias="_title")] = UNSET
    r"""Title of entity"""
    updated_at: Annotated[OptionalNullable[datetime], pydantic.Field(alias="_updated_at")] = UNSET
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["_acl", "_created_at", "_id", "_org", "_owners", "_schema", "_tags", "_title", "_updated_at"]
        nullable_fields = ["_created_at", "_tags", "_title", "_updated_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
