"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import metadata as shared_metadata
from ..shared import price as shared_price
from ..shared import product as shared_product
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import List, Optional, Union

class PriceItemDtoType(str, Enum):
    r"""One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."""
    ONE_TIME = 'one_time'
    RECURRING = 'recurring'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PriceItemDtoInput:
    r"""Represents a valid base price item from a client."""
    price: Optional[shared_price.Price] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_price'), 'exclude': lambda f: f is None }})
    r"""The snapshot of the price linked to the price item."""
    product: Optional[shared_product.ProductInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_product'), 'exclude': lambda f: f is None }})
    r"""The snapshot of the product."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""An arbitrary string attached to the price item. Often useful for displaying to users. Defaults to product name."""
    is_composite_price: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_composite_price'), 'exclude': lambda f: f is None }})
    r"""The flag for prices that contain price components."""
    metadata: Optional[List[Union[shared_metadata.MetaData1]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A set of key-value pairs used to store meta data information about an entity."""
    price_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price_id'), 'exclude': lambda f: f is None }})
    r"""The id of the price."""
    product_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_id'), 'exclude': lambda f: f is None }})
    r"""The id of the product."""
    quantity: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    r"""The quantity of products being purchased."""
    type: Optional[PriceItemDtoType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."""
    unit_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount'), 'exclude': lambda f: f is None }})
    r"""The unit amount value"""
    unit_amount_decimal: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount_decimal'), 'exclude': lambda f: f is None }})
    r"""The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places."""
    

