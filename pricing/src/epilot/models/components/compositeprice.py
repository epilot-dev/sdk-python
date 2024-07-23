"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .price import Price
from .pricecomponentrelation import PriceComponentRelation
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Two:
    dollar_relation: Optional[List[PriceComponentRelation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompositePrice:
    r"""The price entity schema for dynamic pricing"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'exclude': lambda f: f is None }})
    r"""The price creation date"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    r"""The price id"""
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org_id'), 'exclude': lambda f: f is None }})
    r"""The organization id the price belongs to"""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""An arbitrary set of tags attached to the composite price"""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title'), 'exclude': lambda f: f is None }})
    r"""The price autogenerated title"""
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'exclude': lambda f: f is None }})
    r"""The price last update date"""
    active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is None }})
    r"""Whether the price can be used for new purchases."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""A brief description of the price."""
    is_composite_price: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_composite_price'), 'exclude': lambda f: f is None }})
    r"""The flag for prices that contain price components."""
    price_components: Optional[PriceComponents] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price_components'), 'exclude': lambda f: f is None }})
    r"""A set of [price](/api/pricing#tag/simple_price_schema) components that define the composite price."""
    unit_amount_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount_currency'), 'exclude': lambda f: f is None }})
    r"""Three-letter ISO currency code, in lowercase."""
    


PriceComponents = Union[List[Price], Two]
