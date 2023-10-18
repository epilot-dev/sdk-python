"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import step as shared_step
from ..shared import updatestepreq as shared_updatestepreq
from typing import Optional


@dataclasses.dataclass
class UpdateStepRequest:
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'executionId', 'style': 'simple', 'explode': False }})
    r"""Id of the execution"""
    step_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'stepId', 'style': 'simple', 'explode': False }})
    r"""Short uuid (length 6) to identify the Workflow Execution Step."""
    update_step_req: shared_updatestepreq.UpdateStepReq = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Workflow Execution Step payload"""
    



@dataclasses.dataclass
class UpdateStepResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Validation Errors"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    step: Optional[shared_step.Step] = dataclasses.field(default=None)
    r"""Success - if the step is updated successfully"""
    

