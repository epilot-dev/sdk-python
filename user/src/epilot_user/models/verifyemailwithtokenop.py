"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userverificationpayload import UserVerificationPayload, UserVerificationPayloadTypedDict
from epilot_user.types import BaseModel
from epilot_user.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class VerifyEmailWithTokenRequestTypedDict(TypedDict):
    token: str
    r"""Verification Token"""
    user_verification_payload: NotRequired[UserVerificationPayloadTypedDict]
    

class VerifyEmailWithTokenRequest(BaseModel):
    token: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    r"""Verification Token"""
    user_verification_payload: Annotated[Optional[UserVerificationPayload], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
