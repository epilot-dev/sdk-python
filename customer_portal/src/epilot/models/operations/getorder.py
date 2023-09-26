"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional



@dataclasses.dataclass
class GetOrderSecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetOrderRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of order"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetOrder200ApplicationJSON:
    r"""The requested order has been retrieved successfully."""
    cross_sellable_products: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('crossSellableProducts'), 'exclude': lambda f: f is None }})
    r"""The related cross sellable products of the requested order"""
    entity: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    r"""The order entity"""
    files: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    r"""The related files of the requested order"""
    products: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products'), 'exclude': lambda f: f is None }})
    r"""The related products of the requested order"""
    relations: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relations'), 'exclude': lambda f: f is None }})
    r"""The related entities of the requested order"""
    workflow: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow'), 'exclude': lambda f: f is None }})
    r"""The related workflows of the requested order"""
    




@dataclasses.dataclass
class GetOrderResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    get_order_200_application_json_object: Optional[GetOrder200ApplicationJSON] = dataclasses.field(default=None)
    r"""The requested order has been retrieved successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

