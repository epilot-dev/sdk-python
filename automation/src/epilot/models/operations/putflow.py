"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import automationflow as shared_automationflow
from typing import Optional


@dataclasses.dataclass
class PutFlowRequest:
    
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flow_id', 'style': 'simple', 'explode': False }})

    r"""Automation Workflow ID"""
    automation_flow_input: Optional[shared_automationflow.AutomationFlowInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    r"""Automation flow to create"""
    

@dataclasses.dataclass
class PutFlowResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)

    r"""The updated automation flow"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    