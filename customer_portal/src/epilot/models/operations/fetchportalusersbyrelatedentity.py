"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityslug as shared_entityslug
from ..shared import errorresp as shared_errorresp
from ..shared import portaluser as shared_portaluser
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclasses.dataclass
class FetchPortalUsersByRelatedEntitySecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class FetchPortalUsersByRelatedEntityRequest:
    entity_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'entity_id', 'style': 'form', 'explode': True }})
    slug: shared_entityslug.EntitySlug = dataclasses.field(metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""URL-friendly identifier for the entity schema"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FetchPortalUsersByRelatedEntity200ApplicationJSON:
    r"""Returns the portal users under the given entity."""
    portal_users: Optional[List[shared_portaluser.PortalUser]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('portalUsers'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class FetchPortalUsersByRelatedEntityResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    fetch_portal_users_by_related_entity_200_application_json_object: Optional[FetchPortalUsersByRelatedEntity200ApplicationJSON] = dataclasses.field(default=None)
    r"""Returns the portal users under the given entity."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

