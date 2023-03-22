"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import maxallowedlimit as shared_maxallowedlimit
from typing import Optional


@dataclasses.dataclass
class GetMaxAllowedLimitResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Other errors"""  
    max_allowed_limit: Optional[shared_maxallowedlimit.MaxAllowedLimit] = dataclasses.field(default=None)
    r"""A combo of current number of workflows, and the max allowed number of workflows."""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    