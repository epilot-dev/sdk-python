"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schema import Schema, SchemaTypedDict
from epilot_customer_portal.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class GetSchemasResponseBodyTypedDict(TypedDict):
    r"""Retrieved schemas for an organization successfully."""
    
    schemas: NotRequired[List[SchemaTypedDict]]
    

class GetSchemasResponseBody(BaseModel):
    r"""Retrieved schemas for an organization successfully."""
    
    schemas: Optional[List[Schema]] = None
    
