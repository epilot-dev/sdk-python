"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import definitionnotfoundresp as shared_definitionnotfoundresp
from ..shared import errorresp as shared_errorresp
from ..shared import workflowdefinition as shared_workflowdefinition
from typing import Optional



@dataclasses.dataclass
class GetDefinitionRequest:
    definition_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'definitionId', 'style': 'simple', 'explode': False }})
    r"""Short uuid (length 8) to identify the Workflow Definition."""
    




@dataclasses.dataclass
class GetDefinitionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    definition_not_found_resp: Optional[shared_definitionnotfoundresp.DefinitionNotFoundResp] = dataclasses.field(default=None)
    r"""Definition Not found"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Validation Errors"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    workflow_definition: Optional[shared_workflowdefinition.WorkflowDefinition] = dataclasses.field(default=None)
    r"""Returns the Workflow definition"""
    

