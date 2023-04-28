"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import closingreasonsids as shared_closingreasonsids
from typing import Optional


@dataclasses.dataclass
class SetWorkflowClosingReasonsRequest:
    
    closing_reasons_ids: shared_closingreasonsids.ClosingReasonsIds = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})

    r"""set all closing reasons for a specific definition"""
    definition_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'definitionId', 'style': 'simple', 'explode': False }})

    r"""ID of a workflow definition"""
    

@dataclasses.dataclass
class SetWorkflowClosingReasonsResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    