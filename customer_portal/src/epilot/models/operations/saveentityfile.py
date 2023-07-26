"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional



@dataclasses.dataclass
class SaveEntityFileSecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SaveEntityFile201ApplicationJSON:
    r"""The files have been saved to the entitiy successfully."""
    created_files: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdFiles'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SaveEntityFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""The request could not be validated"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    save_entity_file_201_application_json_object: Optional[SaveEntityFile201ApplicationJSON] = dataclasses.field(default=None)
    r"""The files have been saved to the entitiy successfully."""
    

