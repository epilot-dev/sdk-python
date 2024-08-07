"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .attachmentsrelation import AttachmentsRelation, AttachmentsRelationTypedDict
from epilot_message.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ThreadTypedDict(TypedDict):
    r"""Open new thread when sending the very first message in conversation. Thread should contains context related to all messages in it (eg. topic, brand_id, opportunity_id, assigned_to,...).            Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing.            `thread` or `parent_id` must be provided either.

    """
    
    topic: str
    r"""Message topic (e.g. which service sends the message or message category)"""
    assigned_to: NotRequired[List[str]]
    r"""Ivy User ID of who the message is assigned to. Default is the user who sends message."""
    

class Thread(BaseModel):
    r"""Open new thread when sending the very first message in conversation. Thread should contains context related to all messages in it (eg. topic, brand_id, opportunity_id, assigned_to,...).            Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing.            `thread` or `parent_id` must be provided either.

    """
    
    topic: str
    r"""Message topic (e.g. which service sends the message or message category)"""
    assigned_to: Optional[List[str]] = None
    r"""Ivy User ID of who the message is assigned to. Default is the user who sends message."""
    

class MessageRequestParamsTypedDict(TypedDict):
    from_: AddressTypedDict
    subject: str
    r"""Subject"""
    bcc: NotRequired[List[AddressTypedDict]]
    r"""Bcc email addresses"""
    cc: NotRequired[List[AddressTypedDict]]
    r"""Cc email addresses"""
    file: NotRequired[AttachmentsRelationTypedDict]
    r"""Message attachments"""
    html: NotRequired[str]
    r"""HTML body"""
    parent_id: NotRequired[str]
    r"""Entity ID of parent message which this message replies to or forwards from.            If both `parent_id` and `thread` are provided, `thread` is discarded.

    """
    reply_to: NotRequired[AddressTypedDict]
    text: NotRequired[str]
    r"""Text body. If not provided, text body is converted from HTML body using [html-to-text](https://www.npmjs.com/package/html-to-text)"""
    thread: NotRequired[ThreadTypedDict]
    r"""Open new thread when sending the very first message in conversation. Thread should contains context related to all messages in it (eg. topic, brand_id, opportunity_id, assigned_to,...).            Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing.            `thread` or `parent_id` must be provided either.

    """
    to: NotRequired[List[AddressTypedDict]]
    r"""To email addresses"""
    

class MessageRequestParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    from_: Annotated[Address, pydantic.Field(alias="from")]
    subject: str
    r"""Subject"""
    bcc: Optional[List[Address]] = None
    r"""Bcc email addresses"""
    cc: Optional[List[Address]] = None
    r"""Cc email addresses"""
    file: Optional[AttachmentsRelation] = None
    r"""Message attachments"""
    html: Optional[str] = None
    r"""HTML body"""
    parent_id: Optional[str] = None
    r"""Entity ID of parent message which this message replies to or forwards from.            If both `parent_id` and `thread` are provided, `thread` is discarded.

    """
    reply_to: Optional[Address] = None
    text: Optional[str] = None
    r"""Text body. If not provided, text body is converted from HTML body using [html-to-text](https://www.npmjs.com/package/html-to-text)"""
    thread: Optional[Thread] = None
    r"""Open new thread when sending the very first message in conversation. Thread should contains context related to all messages in it (eg. topic, brand_id, opportunity_id, assigned_to,...).            Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing.            `thread` or `parent_id` must be provided either.

    """
    to: Optional[List[Address]] = None
    r"""To email addresses"""
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    
