"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import workflowdefinition as shared_workflowdefinition
from typing import Optional



@dataclasses.dataclass
class GetDefinitionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Other errors"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    workflow_definitions: Optional[list[shared_workflowdefinition.WorkflowDefinition]] = dataclasses.field(default=None)
    r"""Success - definitions loaded with success. Empty array if org has no definitions."""
    

