"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_message.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class EmailType(str, Enum):
    r"""Type of the email, Internal (360 Agents), Partners, External users(Customers)

    """
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    PARTNER = "PARTNER"

class SendErrorTypedDict(TypedDict):
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.            JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>

    """
    
    

class SendError(BaseModel):
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.            JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>

    """
    
    

class SendStatus(str, Enum):
    r"""Sent message status regarding to this recipient.            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>

    """
    SEND = "SEND"
    DELIVERY = "DELIVERY"
    REJECT = "REJECT"
    COMPLAINT = "COMPLAINT"
    BOUNCE = "BOUNCE"
    ERROR = "ERROR"

class AddressTypedDict(TypedDict):
    address: str
    r"""Email address"""
    email_type: NotRequired[Nullable[EmailType]]
    r"""Type of the email, Internal (360 Agents), Partners, External users(Customers)

    """
    name: NotRequired[str]
    r"""Email address alias"""
    send_error: NotRequired[SendErrorTypedDict]
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.            JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>

    """
    send_status: NotRequired[SendStatus]
    r"""Sent message status regarding to this recipient.            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>

    """
    

class Address(BaseModel):
    address: str
    r"""Email address"""
    email_type: OptionalNullable[EmailType] = UNSET
    r"""Type of the email, Internal (360 Agents), Partners, External users(Customers)

    """
    name: Optional[str] = None
    r"""Email address alias"""
    send_error: Optional[SendError] = None
    r"""Information about reject, complaint or bounce event. Only available if `send_status` is REJECT, COMPLAINT, BOUNCE or ERROR.            JSON object is defined by AWS SES. Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notification-contents.html>

    """
    send_status: Optional[SendStatus] = None
    r"""Sent message status regarding to this recipient.            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>

    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email_type", "name", "send_error", "send_status"]
        nullable_fields = ["email_type"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
