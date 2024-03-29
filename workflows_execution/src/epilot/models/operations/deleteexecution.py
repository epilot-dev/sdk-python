"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from typing import Optional


@dataclasses.dataclass
class DeleteExecutionRequest:
    
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'executionId', 'style': 'simple', 'explode': False }})
    r"""Id of the execution to de deleted."""  
    

@dataclasses.dataclass
class DeleteExecutionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Failed to authenticate"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    