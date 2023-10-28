"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SalesTax(str, Enum):
    r"""The default tax rate applicable to the product.
    This field is deprecated, use the new `tax` attribute.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    NONTAXABLE = 'nontaxable'
    REDUCED = 'reduced'
    STANDARD = 'standard'
