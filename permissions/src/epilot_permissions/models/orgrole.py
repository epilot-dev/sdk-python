"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .grant import Grant, GrantTypedDict
from datetime import datetime
from enum import Enum
from epilot_permissions.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class OrgRoleType(str, Enum):
    ORG_ROLE = "org_role"

class OrgRoleTypedDict(TypedDict):
    r"""A role automatically applied to all users in an organization."""
    
    grants: List[GrantTypedDict]
    r"""List of grants (permissions) applied to the role"""
    id: str
    r"""Format: <organization_id>:<slug>"""
    name: str
    r"""Human-friendly name for the role"""
    organization_id: str
    r"""Id of an organization"""
    slug: str
    r"""URL-friendly name for the role"""
    type: OrgRoleType
    expires_at: NotRequired[datetime]
    r"""date and time then the role will expire"""
    pricing_tier: NotRequired[str]
    r"""The pricing tier of the organization this root role is based on"""
    

class OrgRole(BaseModel):
    r"""A role automatically applied to all users in an organization."""
    
    grants: List[Grant]
    r"""List of grants (permissions) applied to the role"""
    id: str
    r"""Format: <organization_id>:<slug>"""
    name: str
    r"""Human-friendly name for the role"""
    organization_id: str
    r"""Id of an organization"""
    slug: str
    r"""URL-friendly name for the role"""
    type: OrgRoleType
    expires_at: Optional[datetime] = None
    r"""date and time then the role will expire"""
    pricing_tier: Optional[str] = None
    r"""The pricing tier of the organization this root role is based on"""
    
