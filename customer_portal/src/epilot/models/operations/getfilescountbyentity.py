"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityfilecount as shared_entityfilecount
from ..shared import errorresp as shared_errorresp
from typing import List, Optional


@dataclasses.dataclass
class GetFilesCountByEntitySecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class GetFilesCountByEntityResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    entity_file_counts: Optional[List[shared_entityfilecount.EntityFileCount]] = dataclasses.field(default=None)
    r"""The file counts have been fetched successfully."""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

