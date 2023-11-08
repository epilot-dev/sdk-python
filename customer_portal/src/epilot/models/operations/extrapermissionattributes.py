"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import extraschemaattributes as components_extraschemaattributes
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclasses.dataclass
class ExtraPermissionAttributesSecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Data:
    contact: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact'), 'exclude': lambda f: f is None }})
    contract: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contract'), 'exclude': lambda f: f is None }})
    meter: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meter'), 'exclude': lambda f: f is None }})
    meter_counter: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meter_counter'), 'exclude': lambda f: f is None }})
    opportunity: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opportunity'), 'exclude': lambda f: f is None }})
    order: Optional[List[components_extraschemaattributes.ExtraSchemaAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExtraPermissionAttributesResponseBody:
    r"""Retrieved extra permission attributes successfully."""
    data: Optional[Data] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class ExtraPermissionAttributesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[ExtraPermissionAttributesResponseBody] = dataclasses.field(default=None)
    r"""Retrieved extra permission attributes successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

