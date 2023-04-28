"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import address as shared_address
from ..shared import attachmentsrelation as shared_attachmentsrelation
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from marshmallow import fields
from typing import Optional

class UpdateMessage201ApplicationJSONSendStatusEnum(str, Enum):
    SEND = 'SEND'
    DELIVERY = 'DELIVERY'
    REJECT = 'REJECT'
    COMPLAINT = 'COMPLAINT'
    BOUNCE = 'BOUNCE'
    ERROR = 'ERROR'

class UpdateMessage201ApplicationJSONTypeEnum(str, Enum):
    r"""Message type"""
    SENT = 'SENT'
    RECEIVED = 'RECEIVED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateMessage201ApplicationJSON:
    r"""Success"""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})

    r"""Created date"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})

    r"""Entity ID"""
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})

    r"""Ivy Organization ID the entity belongs to"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})

    r"""URL-friendly identifier for the entity schema"""
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})

    r"""Entity title"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})

    r"""Updated date"""
    from_: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from') }})

    subject: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subject') }})

    r"""Subject"""
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})

    r"""Entity tags"""
    bcc: Optional[list[shared_address.Address]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bcc'), 'exclude': lambda f: f is None }})

    r"""Bcc email addresses"""
    cc: Optional[list[shared_address.Address]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cc'), 'exclude': lambda f: f is None }})

    r"""Cc email addresses"""
    file: Optional[shared_attachmentsrelation.AttachmentsRelation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file'), 'exclude': lambda f: f is None }})

    r"""Message attachments"""
    html: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html'), 'exclude': lambda f: f is None }})

    r"""HTML body"""
    in_reply_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_reply_to'), 'exclude': lambda f: f is None }})

    r"""In-Reply-To header. Value is the `message_id` of parent message."""
    message_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_id'), 'exclude': lambda f: f is None }})

    r"""Message ID which is from email provider. If you provide `message-id`, API overrides by its own value."""
    org_read_message: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_read_message'), 'exclude': lambda f: f is None }})

    r"""Ivy Organization ID of organization read the message."""
    references: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('references'), 'exclude': lambda f: f is None }})

    r"""References header. Value is the series of `message_id` which is reparated by space to indicate that message has parent.\ 
    The last message ID in references identifies the parent. The first message ID in references identifies the first message in the thread.\
    The basic idea is that sender should copy `references` from the parent and append the parent's `message_id` when replying.
    """
    reply_to: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reply_to'), 'exclude': lambda f: f is None }})

    send_status: Optional[list[UpdateMessage201ApplicationJSONSendStatusEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('send_status'), 'exclude': lambda f: f is None }})

    r"""Sent message status. The array contains sending message status corresponding to all recipients. For more detail, check `send_status` of each recipient in `to`, `cc`, `bcc`\ 
    Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>
    """
    sender: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sender'), 'exclude': lambda f: f is None }})

    r"""Ivy User ID of user sends the message."""
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})

    r"""Text body"""
    to: Optional[list[shared_address.Address]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})

    r"""To email addresses"""
    type: Optional[UpdateMessage201ApplicationJSONTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})

    r"""Message type"""
    user_read_message: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_read_message'), 'exclude': lambda f: f is None }})

    r"""Ivy User ID of user read the message."""
    

@dataclasses.dataclass
class UpdateMessageResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    update_message_201_application_json_object: Optional[UpdateMessage201ApplicationJSON] = dataclasses.field(default=None)

    r"""Success"""
    