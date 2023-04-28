"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import workflowexecution as shared_workflowexecution
from typing import Optional


@dataclasses.dataclass
class CreateExecutionResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)

    r"""Validation Errors"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    workflow_execution: Optional[shared_workflowexecution.WorkflowExecution] = dataclasses.field(default=None)

    r"""Success - if the execution is created successfully"""
    