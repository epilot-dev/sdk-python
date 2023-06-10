"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional



@dataclasses.dataclass
class AddressSendError:
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.\ 
    JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>
    """
    pass

class AddressSendStatus(str, Enum):
    r"""Sent message status regarding to this recipient.\ 
    Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>
    """
    SEND = 'SEND'
    DELIVERY = 'DELIVERY'
    REJECT = 'REJECT'
    COMPLAINT = 'COMPLAINT'
    BOUNCE = 'BOUNCE'
    ERROR = 'ERROR'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Address:
    address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Email address"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Email address alias"""
    send_error: Optional[AddressSendError] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('send_error'), 'exclude': lambda f: f is None }})
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.\ 
    JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>
    """
    send_status: Optional[AddressSendStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('send_status'), 'exclude': lambda f: f is None }})
    r"""Sent message status regarding to this recipient.\ 
    Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>
    """
    

