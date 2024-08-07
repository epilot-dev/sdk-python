"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityimportparams as shared_entityimportparams
from typing import Optional


@dataclasses.dataclass
class ImportEntitiesRequest:
    entity_import_params: Optional[shared_entityimportparams.EntityImportParams] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    r"""The ID of the import job. This ID is used to track the progress and fetch the result of the import operation."""
    



@dataclasses.dataclass
class ImportEntitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

