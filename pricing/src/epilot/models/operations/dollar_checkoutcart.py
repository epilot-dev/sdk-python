"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import checkoutcart as shared_checkoutcart
from ..shared import checkoutcartresult as shared_checkoutcartresult
from typing import Any, Optional


@dataclasses.dataclass
class DollarCheckoutCartRequest:
    
    checkout_cart: shared_checkoutcart.CheckoutCart = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    x_ivy_org_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Ivy-Org-ID', 'style': 'simple', 'explode': False }})
    r"""The target Organization Id represented by the caller"""  
    

@dataclasses.dataclass
class DollarCheckoutCartResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    checkout_cart_result: Optional[shared_checkoutcartresult.CheckoutCartResult] = dataclasses.field(default=None)
    r"""The checkout result"""  
    error: Optional[Any] = dataclasses.field(default=None)
    r"""Invalid payload"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    