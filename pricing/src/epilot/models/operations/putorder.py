"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import order as components_order
from ...models.components import orderpayload as components_orderpayload
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class PutOrderRequest:
    order_payload: components_orderpayload.OrderPayload = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Order entity ID"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutOrderResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    order: Optional[components_order.Order] = dataclasses.field(default=None)
    r"""Order result"""
    

