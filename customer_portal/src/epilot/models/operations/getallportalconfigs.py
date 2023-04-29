"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import portalconfig as shared_portalconfig
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllPortalConfigs200ApplicationJSON:
    r"""ok"""
    
    data: Optional[list[shared_portalconfig.PortalConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetAllPortalConfigsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_all_portal_configs_200_application_json_object: Optional[GetAllPortalConfigs200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    