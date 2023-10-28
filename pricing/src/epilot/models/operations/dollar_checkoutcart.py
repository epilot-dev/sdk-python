"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import checkoutcart as shared_checkoutcart
from ..shared import checkoutcartresult as shared_checkoutcartresult
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class DollarCheckoutCartRequest:
    checkout_cart: shared_checkoutcart.CheckoutCart = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    x_ivy_org_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Ivy-Org-ID', 'style': 'simple', 'explode': False }})
    r"""The target Organization Id represented by the caller"""
    



@dataclasses.dataclass
class DollarCheckoutCartResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    checkout_cart_result: Optional[shared_checkoutcartresult.CheckoutCartResult] = dataclasses.field(default=None)
    r"""The checkout result"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Invalid payload"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

