"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetOrderSecurity:
    
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetOrderRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The Id of order"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrder200ApplicationJSON:
    r"""The returned order"""
    
    cross_sellable_products: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('crossSellableProducts'), 'exclude': lambda f: f is None }})
    entity: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    files: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    products: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products'), 'exclude': lambda f: f is None }})
    relations: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relations'), 'exclude': lambda f: f is None }})
    workflow: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetOrderResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_order_200_application_json_object: Optional[GetOrder200ApplicationJSON] = dataclasses.field(default=None)
    r"""The returned order"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    