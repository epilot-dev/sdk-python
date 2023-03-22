"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import changereasonstatusreq as shared_changereasonstatusreq
from ..shared import errorresp as shared_errorresp
from typing import Optional


@dataclasses.dataclass
class ChangeReasonStatusRequest:
    
    reason_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'reasonId', 'style': 'simple', 'explode': False }})  
    change_reason_status_req: Optional[shared_changereasonstatusreq.ChangeReasonStatusReq] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""change the status of a closing reason"""  
    

@dataclasses.dataclass
class ChangeReasonStatusResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""bad request"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    