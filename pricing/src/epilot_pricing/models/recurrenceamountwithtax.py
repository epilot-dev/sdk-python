"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_pricing.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class RecurrenceAmountWithTaxBillingPeriod(str, Enum):
    r"""The price billing period."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    EVERY_QUARTER = "every_quarter"
    EVERY_6_MONTHS = "every_6_months"
    YEARLY = "yearly"

class RecurrenceAmountWithTaxTaxTypedDict(TypedDict):
    r"""The taxes applied to the price item."""
    
    

class RecurrenceAmountWithTaxTax(BaseModel):
    r"""The taxes applied to the price item."""
    
    

class RecurrenceAmountWithTaxTypedDict(TypedDict):
    r"""An amount associated with a specific recurrence."""
    
    amount_subtotal: int
    r"""Total amount of items with same recurrence, excluding taxes."""
    amount_total: int
    r"""Total amount of items with same recurrence."""
    amount_tax: NotRequired[int]
    r"""Total tax amount of items with same recurrence."""
    billing_period: NotRequired[RecurrenceAmountWithTaxBillingPeriod]
    r"""The price billing period."""
    tax: NotRequired[RecurrenceAmountWithTaxTaxTypedDict]
    r"""The taxes applied to the price item."""
    type: NotRequired[str]
    r"""The price type."""
    

class RecurrenceAmountWithTax(BaseModel):
    r"""An amount associated with a specific recurrence."""
    
    amount_subtotal: int
    r"""Total amount of items with same recurrence, excluding taxes."""
    amount_total: int
    r"""Total amount of items with same recurrence."""
    amount_tax: Optional[int] = None
    r"""Total tax amount of items with same recurrence."""
    billing_period: Optional[RecurrenceAmountWithTaxBillingPeriod] = None
    r"""The price billing period."""
    tax: Optional[RecurrenceAmountWithTaxTax] = None
    r"""The taxes applied to the price item."""
    type: Optional[str] = None
    r"""The price type."""
    