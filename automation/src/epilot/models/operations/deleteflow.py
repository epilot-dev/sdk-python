"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import automationflow as shared_automationflow
from typing import Optional



@dataclasses.dataclass
class DeleteFlowRequest:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flow_id', 'style': 'simple', 'explode': False }})
    r"""Automation Workflow ID"""
    




@dataclasses.dataclass
class DeleteFlowResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    r"""The deleted automation flow"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

