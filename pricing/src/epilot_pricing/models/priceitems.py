"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .compositepriceitem import CompositePriceItem, CompositePriceItemTypedDict
from .priceitem import PriceItem, PriceItemTypedDict
from typing import Union


PriceItemsTypedDict = Union[CompositePriceItemTypedDict, PriceItemTypedDict]


PriceItems = Union[CompositePriceItem, PriceItem]

