"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityslug as shared_entityslug
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional



@dataclasses.dataclass
class GetEntitiesByIdentifiersSecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetEntitiesByIdentifiersRequest:
    request_body: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""The entities are retrieved successfully."""
    slug: shared_entityslug.EntitySlug = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""The slug of an entity"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetEntitiesByIdentifiers200ApplicationJSON:
    r"""The returned Entities"""
    data: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetEntitiesByIdentifiersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""The request could not be validated"""
    get_entities_by_identifiers_200_application_json_object: Optional[GetEntitiesByIdentifiers200ApplicationJSON] = dataclasses.field(default=None)
    r"""The returned Entities"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

