"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import uploadfilepayload as shared_uploadfilepayload
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class UploadFileRequest:
    
    file_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'file_entity_id', 'style': 'form', 'explode': True }})
    r"""file entity id"""
    upload_file_payload: Optional[shared_uploadfilepayload.UploadFilePayload] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadFile201ApplicationJSONS3ref:
    
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadFile201ApplicationJSON:
    r"""Pre-signed URL for POST / PUT upload"""
    
    public_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_url'), 'exclude': lambda f: f is None }})
    r"""Returned only if file is permanent i.e. file_entity_id is passed"""
    s3ref: Optional[UploadFile201ApplicationJSONS3ref] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})
    upload_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upload_url'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UploadFileResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    upload_file_201_application_json_object: Optional[UploadFile201ApplicationJSON] = dataclasses.field(default=None)
    r"""Pre-signed URL for POST / PUT upload"""
    