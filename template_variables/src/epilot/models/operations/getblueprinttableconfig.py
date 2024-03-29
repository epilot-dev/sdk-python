"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import customvariable as shared_customvariable
from typing import Optional


@dataclasses.dataclass
class GetBluePrintTableConfigResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    custom_variable: Optional[shared_customvariable.CustomVariable] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    