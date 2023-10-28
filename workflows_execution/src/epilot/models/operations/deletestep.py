"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from typing import Optional


@dataclasses.dataclass
class DeleteStepRequest:
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'executionId', 'style': 'simple', 'explode': False }})
    r"""Id of the execution"""
    step_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'stepId', 'style': 'simple', 'explode': False }})
    r"""Short uuid (length 6) to identify the Workflow Execution Step."""
    



@dataclasses.dataclass
class DeleteStepResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Other errors"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

