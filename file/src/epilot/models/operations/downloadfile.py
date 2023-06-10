"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional



@dataclasses.dataclass
class DownloadFileRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    attachment: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'attachment', 'style': 'form', 'explode': True }})
    r"""Controls the Content-Disposition header to control browser behaviour. Set to true to trigger download."""
    version: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'version', 'style': 'form', 'explode': True }})
    r"""index of file version"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DownloadFile200ApplicationJSON:
    r"""Generated thumbnail image"""
    download_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('download_url'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class DownloadFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    download_file_200_application_json_object: Optional[DownloadFile200ApplicationJSON] = dataclasses.field(default=None)
    r"""Generated thumbnail image"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

