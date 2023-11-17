"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import automationexecution as components_automationexecution
from typing import Optional


@dataclasses.dataclass
class GetExecutionRequest:
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'execution_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetExecutionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    automation_execution: Optional[components_automationexecution.AutomationExecution] = dataclasses.field(default=None)
    r"""The returned execution"""
    

