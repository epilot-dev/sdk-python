"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import origin as components_origin
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class LoginToPortalAsUserSecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoginToPortalAsUserRequestBody:
    r"""The request body to log in to a portal impersonating a user"""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""The email address of the user to log in as"""
    origin: Optional[components_origin.Origin] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin'), 'exclude': lambda f: f is None }})
    r"""Origin of the portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoginToPortalAsUserResponseBody:
    r"""The token has been generated successfully."""
    login_as_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('login_as_token'), 'exclude': lambda f: f is None }})
    r"""A generated login_as_token to log in to a portal impersonating a user."""
    



@dataclasses.dataclass
class LoginToPortalAsUserResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[LoginToPortalAsUserResponseBody] = dataclasses.field(default=None)
    r"""The token has been generated successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

