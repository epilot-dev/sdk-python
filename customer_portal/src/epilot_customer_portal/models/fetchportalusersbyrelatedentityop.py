"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityslug import EntitySlug
from .portaluser import PortalUser, PortalUserTypedDict
from epilot_customer_portal.types import BaseModel
from epilot_customer_portal.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class FetchPortalUsersByRelatedEntityRequestTypedDict(TypedDict):
    entity_id: str
    slug: EntitySlug
    r"""URL-friendly identifier for the entity schema"""
    

class FetchPortalUsersByRelatedEntityRequest(BaseModel):
    entity_id: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    slug: Annotated[EntitySlug, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    r"""URL-friendly identifier for the entity schema"""
    

class FetchPortalUsersByRelatedEntityResponseBodyTypedDict(TypedDict):
    r"""Returns the portal users under the given entity."""
    
    portal_users: NotRequired[List[PortalUserTypedDict]]
    

class FetchPortalUsersByRelatedEntityResponseBody(BaseModel):
    r"""Returns the portal users under the given entity."""
    
    portal_users: Annotated[Optional[List[PortalUser]], pydantic.Field(alias="portalUsers")] = None
    
