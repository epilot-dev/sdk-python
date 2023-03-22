"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import automationexecution as shared_automationexecution
from typing import Optional


@dataclasses.dataclass
class GetExecutionRequest:
    
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'execution_id', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetExecutionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    automation_execution: Optional[shared_automationexecution.AutomationExecution] = dataclasses.field(default=None)
    r"""The returned execution"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    