"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .changereasonstatusreq import ChangeReasonStatusReq, ChangeReasonStatusReqTypedDict
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ChangeReasonStatusRequestTypedDict(TypedDict):
    reason_id: str
    change_reason_status_req: NotRequired[ChangeReasonStatusReqTypedDict]
    r"""change the status of a closing reason"""
    

class ChangeReasonStatusRequest(BaseModel):
    reason_id: Annotated[str, pydantic.Field(alias="reasonId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    change_reason_status_req: Annotated[Optional[ChangeReasonStatusReq], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    r"""change the status of a closing reason"""
    
