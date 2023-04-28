"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import closingreasonresp as shared_closingreasonresp
from ..shared import errorresp as shared_errorresp
from typing import Optional


@dataclasses.dataclass
class GetClosingReasonExecutionRequest:
    
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'executionId', 'style': 'simple', 'explode': False }})

    r"""Id of the execution"""
    

@dataclasses.dataclass
class GetClosingReasonExecutionResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    closing_reason_resp: Optional[shared_closingreasonresp.ClosingReasonResp] = dataclasses.field(default=None)

    r"""returns all Closing Reasons for this Execution"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)

    r"""Internal Issues"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    