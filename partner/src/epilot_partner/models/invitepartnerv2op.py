"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .partnerinvitationpayload import PartnerInvitationPayload, PartnerInvitationPayloadTypedDict
from epilot_partner.types import BaseModel
from epilot_partner.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class InvitePartnerV2RequestTypedDict(TypedDict):
    id: str
    r"""The Id of partner"""
    partner_invitation_payload: NotRequired[PartnerInvitationPayloadTypedDict]
    

class InvitePartnerV2Request(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The Id of partner"""
    partner_invitation_payload: Annotated[Optional[PartnerInvitationPayload], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
