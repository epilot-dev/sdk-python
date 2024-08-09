"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_file.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class PublicLinkTypedDict(TypedDict):
    id: NotRequired[str]
    r"""ID of the public link"""
    last_accessed_at: NotRequired[str]
    r"""The most recent timestamp when the file was accessed"""
    link: NotRequired[str]
    r"""Public link of the file"""
    

class PublicLink(BaseModel):
    id: Optional[str] = None
    r"""ID of the public link"""
    last_accessed_at: Optional[str] = None
    r"""The most recent timestamp when the file was accessed"""
    link: Optional[str] = None
    r"""Public link of the file"""
    
