"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .message import Message, MessageTypedDict
from datetime import datetime
from epilot_message.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateThreadResponseBodyTypedDict(TypedDict):
    r"""Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing."""
    
    created_at: datetime
    r"""Created date"""
    id: str
    r"""Entity ID"""
    org: str
    r"""Ivy Organization ID the entity belongs to"""
    schema_: str
    r"""URL-friendly identifier for the entity schema"""
    title: str
    r"""Entity title"""
    updated_at: datetime
    r"""Updated date"""
    topic: str
    r"""Message topic (e.g. which service sends the message or message category)"""
    tags: NotRequired[List[str]]
    r"""Entity tags"""
    assigned_to: NotRequired[List[str]]
    r"""Ivy User ID of who the message is assigned to. Default is the user who sends message."""
    latest_message: NotRequired[MessageTypedDict]
    latest_message_at: NotRequired[str]
    r"""The date of the latest message time in the thread"""
    latest_trash_message: NotRequired[MessageTypedDict]
    org_read_message: NotRequired[List[str]]
    r"""Ivy Organization ID of organization read the message."""
    

class UpdateThreadResponseBody(BaseModel):
    r"""Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing."""
    
    created_at: Annotated[datetime, pydantic.Field(alias="_created_at")]
    r"""Created date"""
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""Entity ID"""
    org: Annotated[str, pydantic.Field(alias="_org")]
    r"""Ivy Organization ID the entity belongs to"""
    schema_: Annotated[str, pydantic.Field(alias="_schema")]
    r"""URL-friendly identifier for the entity schema"""
    title: Annotated[str, pydantic.Field(alias="_title")]
    r"""Entity title"""
    updated_at: Annotated[datetime, pydantic.Field(alias="_updated_at")]
    r"""Updated date"""
    topic: str
    r"""Message topic (e.g. which service sends the message or message category)"""
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    r"""Entity tags"""
    assigned_to: Optional[List[str]] = None
    r"""Ivy User ID of who the message is assigned to. Default is the user who sends message."""
    latest_message: Optional[Message] = None
    latest_message_at: Optional[str] = None
    r"""The date of the latest message time in the thread"""
    latest_trash_message: Optional[Message] = None
    org_read_message: Optional[List[str]] = None
    r"""Ivy Organization ID of organization read the message."""
    
