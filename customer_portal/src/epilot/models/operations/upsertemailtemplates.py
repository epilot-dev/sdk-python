"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import emailtemplates as shared_emailtemplates
from ..shared import errorresp as shared_errorresp
from ..shared import origin as shared_origin
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Final, Optional



@dataclasses.dataclass
class UpsertEmailTemplatesSecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class UpsertEmailTemplatesRequest:
    email_templates: shared_emailtemplates.EmailTemplates = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Email templates payload"""
    origin: shared_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpsertEmailTemplates200ApplicationJSON:
    r"""Upserted email templates of the portal successfully."""
    email_templates: shared_emailtemplates.EmailTemplates = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTemplates') }})
    r"""Email templates used for authentication and internal processes"""
    MESSAGE: Final[str] = dataclasses.field(default='Email Templates upserted successfully', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    




@dataclasses.dataclass
class UpsertEmailTemplatesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    upsert_email_templates_200_application_json_object: Optional[UpsertEmailTemplates200ApplicationJSON] = dataclasses.field(default=None)
    r"""Upserted email templates of the portal successfully."""
    

