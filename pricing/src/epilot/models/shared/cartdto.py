"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import customer as shared_customer
from ..shared import metadata as shared_metadata
from ..shared import ordersource as shared_ordersource
from ..shared import orderstatus as shared_orderstatus
from ..shared import paymentmethod as shared_paymentmethod
from ..shared import priceitemdto as shared_priceitemdto
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CartDto:
    r"""A valid cart payload from a client."""
    line_items: List[Union[shared_priceitemdto.PriceItemDtoInput]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line_items') }})
    r"""A valid set of product prices, quantities, (discounts) and taxes from a client."""
    additional_addresses: Optional[List[shared_address.Address]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_addresses'), 'exclude': lambda f: f is None }})
    billing_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    consents: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consents'), 'exclude': lambda f: f is None }})
    customer: Optional[shared_customer.Customer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer'), 'exclude': lambda f: f is None }})
    delivery_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delivery_address'), 'exclude': lambda f: f is None }})
    files: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    r"""An array of file IDs, already upload into the File API, that are related with this cart"""
    journey_data: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journey_data'), 'exclude': lambda f: f is None }})
    metadata: Optional[List[Union[shared_metadata.MetaData1]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A set of key-value pairs used to store meta data information about an entity."""
    payment_method: Optional[shared_paymentmethod.PaymentMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is None }})
    r"""A PaymentMethod represent your customer's payment instruments."""
    source: Optional[shared_ordersource.OrderSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The order generation source"""
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id'), 'exclude': lambda f: f is None }})
    r"""identifier for source e.g. journey ID"""
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_type'), 'exclude': lambda f: f is None }})
    r"""type of source, e.g. journey or manual"""
    status: Optional[shared_orderstatus.OrderStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""| status      | description |
    |-------------|-------|
    | `draft`     | \u200B\u200BStarting state for all orders, at this point we can still edit the order |
    | `quote`     | The order is in a quoting phase, bound to an expiration date |
    | `placed`    | The order has been paid and can now be fulfilled (shipped, delivered, complete) or canceled |
    | `cancelled` | The order has been cancelled |
    | `completed` | The order is now closed and finalized |
    """
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    

