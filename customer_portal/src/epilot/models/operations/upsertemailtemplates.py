"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import emailtemplates as shared_emailtemplates
from ..shared import origin_enum as shared_origin_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class UpsertEmailTemplatesSecurity:
    
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclasses.dataclass
class UpsertEmailTemplatesRequest:
    
    email_templates: shared_emailtemplates.EmailTemplates = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Portal payload"""  
    origin: shared_origin_enum.OriginEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertEmailTemplates200ApplicationJSON:
    r"""ok"""
    
    email_templates: Optional[shared_emailtemplates.EmailTemplates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTemplates'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class UpsertEmailTemplatesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    upsert_email_templates_200_application_json_object: Optional[UpsertEmailTemplates200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""  
    