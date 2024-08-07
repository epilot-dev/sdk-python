"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .order import Order, OrderTypedDict
from epilot_customer_portal.types import BaseModel
from epilot_customer_portal.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateOrderRequestTypedDict(TypedDict):
    id: str
    r"""The ID of order"""
    request_body: NotRequired[Dict[str, Any]]
    

class UpdateOrderRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of order"""
    request_body: Annotated[Optional[Dict[str, Any]], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class UpdateOrderResponseBodyTypedDict(TypedDict):
    r"""Updated the order details successfully."""
    
    data: NotRequired[OrderTypedDict]
    r"""The order entity"""
    

class UpdateOrderResponseBody(BaseModel):
    r"""Updated the order details successfully."""
    
    data: Optional[Order] = None
    r"""The order entity"""
    
