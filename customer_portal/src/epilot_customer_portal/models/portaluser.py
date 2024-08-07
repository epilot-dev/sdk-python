"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from epilot_customer_portal.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PortalUserSchema(str, Enum):
    PORTAL_USER = "portal_user"

class PortalUserTypedDict(TypedDict):
    r"""The portal user entity"""
    
    created_at: datetime
    r"""Creation timestamp of the entity"""
    id: str
    r"""Entity ID"""
    org: str
    r"""Organization ID the entity belongs to"""
    schema_: PortalUserSchema
    title: str
    r"""Title of the entity"""
    updated_at: datetime
    r"""Last update timestamp of the entity"""
    tags: NotRequired[List[str]]
    r"""Array of entity tags"""
    

class PortalUser(BaseModel):
    r"""The portal user entity"""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    created_at: Annotated[datetime, pydantic.Field(alias="_created_at")]
    r"""Creation timestamp of the entity"""
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""Entity ID"""
    org: Annotated[str, pydantic.Field(alias="_org")]
    r"""Organization ID the entity belongs to"""
    schema_: Annotated[PortalUserSchema, pydantic.Field(alias="_schema")]
    title: Annotated[str, pydantic.Field(alias="_title")]
    r"""Title of the entity"""
    updated_at: Annotated[datetime, pydantic.Field(alias="_updated_at")]
    r"""Last update timestamp of the entity"""
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    r"""Array of entity tags"""
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    
