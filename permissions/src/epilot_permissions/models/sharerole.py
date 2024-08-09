"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .grant import Grant, GrantTypedDict
from datetime import datetime
from enum import Enum
from epilot_permissions.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ShareRoleType(str, Enum):
    SHARE_ROLE = "share_role"

class ShareRoleTypedDict(TypedDict):
    r"""A role that can be assigned to users in other organizations for sharing purposes."""
    
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
    type: ShareRoleType
    expires_at: NotRequired[datetime]
    r"""date and time then the role will expire"""
    

class ShareRole(BaseModel):
    r"""A role that can be assigned to users in other organizations for sharing purposes."""
    
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
    type: ShareRoleType
    expires_at: Optional[datetime] = None
    r"""date and time then the role will expire"""
    