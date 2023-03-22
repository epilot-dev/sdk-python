"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import origin_enum as shared_origin_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class ReplaceECPTemplateVariablesSecurity:
    
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplaceECPTemplateVariablesRequestBody:
    r"""ECPVariables payload"""
    
    contact_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactId'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ReplaceECPTemplateVariablesRequest:
    
    origin: shared_origin_enum.OriginEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""  
    request_body: ReplaceECPTemplateVariablesRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""ECPVariables payload"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplaceECPTemplateVariables200ApplicationJSONPortalUser:
    
    invitation_link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitationLink'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplaceECPTemplateVariables200ApplicationJSON:
    r"""ok"""
    
    portal_user: Optional[ReplaceECPTemplateVariables200ApplicationJSONPortalUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('portalUser'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ReplaceECPTemplateVariablesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    replace_ecp_template_variables_200_application_json_object: Optional[ReplaceECPTemplateVariables200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""  
    