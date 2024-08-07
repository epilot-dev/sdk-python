"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .attachmentsrelation import AttachmentsRelation, AttachmentsRelationTypedDict
from datetime import datetime
from enum import Enum
from epilot_message.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SendDraftSendStatus(str, Enum):
    SEND = "SEND"
    DELIVERY = "DELIVERY"
    REJECT = "REJECT"
    COMPLAINT = "COMPLAINT"
    BOUNCE = "BOUNCE"
    ERROR = "ERROR"

class SendDraftType(str, Enum):
    r"""Message type"""
    SENT = "SENT"
    RECEIVED = "RECEIVED"

class SendDraftResponseBodyTypedDict(TypedDict):
    r"""Success"""
    
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
    from_: AddressTypedDict
    subject: str
    r"""Subject"""
    tags: NotRequired[List[str]]
    r"""Entity tags"""
    bcc: NotRequired[List[AddressTypedDict]]
    r"""Bcc email addresses"""
    cc: NotRequired[List[AddressTypedDict]]
    r"""Cc email addresses"""
    file: NotRequired[AttachmentsRelationTypedDict]
    r"""Message attachments"""
    html: NotRequired[str]
    r"""HTML body"""
    in_reply_to: NotRequired[str]
    r"""In-Reply-To header. Value is the `message_id` of parent message.

    """
    message_id: NotRequired[str]
    r"""Message ID which is from email provider. If you provide `message-id`, API overrides by its own value."""
    org_read_message: NotRequired[List[str]]
    r"""Ivy Organization ID of organization read the message."""
    references: NotRequired[str]
    r"""References header. Value is the series of `message_id` which is reparated by space to indicate that message has parent.            The last message ID in references identifies the parent. The first message ID in references identifies the first message in the thread.            The basic idea is that sender should copy `references` from the parent and append the parent's `message_id` when replying.

    """
    reply_to: NotRequired[AddressTypedDict]
    send_status: NotRequired[List[SendDraftSendStatus]]
    r"""Sent message status. The array contains sending message status corresponding to all recipients. For more detail, check `send_status` of each recipient in `to`, `cc`, `bcc`            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>

    """
    sender: NotRequired[str]
    r"""Ivy User ID of user sends the message."""
    text: NotRequired[str]
    r"""Text body"""
    to: NotRequired[List[AddressTypedDict]]
    r"""To email addresses"""
    type: NotRequired[SendDraftType]
    r"""Message type"""
    user_read_message: NotRequired[List[str]]
    r"""Ivy User ID of user read the message."""
    

class SendDraftResponseBody(BaseModel):
    r"""Success"""
    
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
    from_: Annotated[Address, pydantic.Field(alias="from")]
    subject: str
    r"""Subject"""
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    r"""Entity tags"""
    bcc: Optional[List[Address]] = None
    r"""Bcc email addresses"""
    cc: Optional[List[Address]] = None
    r"""Cc email addresses"""
    file: Optional[AttachmentsRelation] = None
    r"""Message attachments"""
    html: Optional[str] = None
    r"""HTML body"""
    in_reply_to: Optional[str] = None
    r"""In-Reply-To header. Value is the `message_id` of parent message.

    """
    message_id: Optional[str] = None
    r"""Message ID which is from email provider. If you provide `message-id`, API overrides by its own value."""
    org_read_message: Optional[List[str]] = None
    r"""Ivy Organization ID of organization read the message."""
    references: Optional[str] = None
    r"""References header. Value is the series of `message_id` which is reparated by space to indicate that message has parent.            The last message ID in references identifies the parent. The first message ID in references identifies the first message in the thread.            The basic idea is that sender should copy `references` from the parent and append the parent's `message_id` when replying.

    """
    reply_to: Optional[Address] = None
    send_status: Optional[List[SendDraftSendStatus]] = None
    r"""Sent message status. The array contains sending message status corresponding to all recipients. For more detail, check `send_status` of each recipient in `to`, `cc`, `bcc`            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>

    """
    sender: Optional[str] = None
    r"""Ivy User ID of user sends the message."""
    text: Optional[str] = None
    r"""Text body"""
    to: Optional[List[Address]] = None
    r"""To email addresses"""
    type: Optional[SendDraftType] = None
    r"""Message type"""
    user_read_message: Optional[List[str]] = None
    r"""Ivy User ID of user read the message."""
    
