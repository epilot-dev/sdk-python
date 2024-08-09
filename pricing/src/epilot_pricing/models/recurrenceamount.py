"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_pricing.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class RecurrenceAmountBillingPeriod(str, Enum):
    r"""The price billing period."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    EVERY_QUARTER = "every_quarter"
    EVERY_6_MONTHS = "every_6_months"
    YEARLY = "yearly"

class RecurrenceAmountTypedDict(TypedDict):
    r"""An amount associated with a specific recurrence."""
    
    amount_subtotal: int
    r"""Total of all items before (discounts or) taxes are applied."""
    amount_subtotal_decimal: str
    r"""Total of all items before (discounts or) taxes are applied, as a string with all the decimal places."""
    amount_total: int
    r"""Total of all items after (discounts and) taxes are applied."""
    amount_total_decimal: str
    r"""Total of all items after (discounts and) taxes are applied, as a string with all the decimal places."""
    amount_tax: NotRequired[int]
    r"""Total of all items taxes, with same recurrence."""
    billing_period: NotRequired[RecurrenceAmountBillingPeriod]
    r"""The price billing period."""
    currency: NotRequired[str]
    r"""Three-letter ISO currency code, in lowercase. Must be a supported currency.
    ISO 4217 CURRENCY CODES as specified in the documentation: https://www.iso.org/iso-4217-currency-codes.html

    """
    type: NotRequired[str]
    r"""The price type."""
    unit_amount_gross: NotRequired[int]
    r"""The unit gross amount value."""
    unit_amount_net: NotRequired[int]
    r"""The unit net amount value."""
    

class RecurrenceAmount(BaseModel):
    r"""An amount associated with a specific recurrence."""
    
    amount_subtotal: int
    r"""Total of all items before (discounts or) taxes are applied."""
    amount_subtotal_decimal: str
    r"""Total of all items before (discounts or) taxes are applied, as a string with all the decimal places."""
    amount_total: int
    r"""Total of all items after (discounts and) taxes are applied."""
    amount_total_decimal: str
    r"""Total of all items after (discounts and) taxes are applied, as a string with all the decimal places."""
    amount_tax: Optional[int] = None
    r"""Total of all items taxes, with same recurrence."""
    billing_period: Optional[RecurrenceAmountBillingPeriod] = None
    r"""The price billing period."""
    currency: Optional[str] = None
    r"""Three-letter ISO currency code, in lowercase. Must be a supported currency.
    ISO 4217 CURRENCY CODES as specified in the documentation: https://www.iso.org/iso-4217-currency-codes.html

    """
    type: Optional[str] = None
    r"""The price type."""
    unit_amount_gross: Optional[int] = None
    r"""The unit gross amount value."""
    unit_amount_net: Optional[int] = None
    r"""The unit net amount value."""
    