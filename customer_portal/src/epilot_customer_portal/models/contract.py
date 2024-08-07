"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from epilot_customer_portal.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BillingPeriod(str, Enum):
    r"""The billing period associated with the contract."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    EVERY_QUARTER = "every_quarter"
    EVERY_6_MONTHS = "every_6_months"
    YEARLY = "yearly"

class Branch(str, Enum):
    r"""The branch associated with the contract."""
    POWER = "power"
    GAS = "gas"
    WATER = "water"
    WASTE_WATER = "waste_water"
    DISTRICT_HEATING = "district_heating"

class NoticeTimeUnit(str, Enum):
    r"""The unit of time for the notice period."""
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"

class RenewalDurationUnit(str, Enum):
    r"""The unit of time for the renewal period."""
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"

class Status(str, Enum):
    r"""The status of the contract."""
    DRAFT = "draft"
    IN_APPROVAL_PROCESS = "in_approval_process"
    APPROVED = "approved"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"
    REVOKED = "revoked"
    TERMINATED = "terminated"
    EXPIRED = "expired"

class ContractTypedDict(TypedDict):
    r"""The contract entity"""
    
    created_at: datetime
    r"""Creation timestamp of the entity"""
    id: str
    r"""Entity ID"""
    org: str
    r"""Organization ID the entity belongs to"""
    title: str
    r"""Title of the entity"""
    updated_at: datetime
    r"""Last update timestamp of the entity"""
    tags: NotRequired[List[str]]
    r"""Array of entity tags"""
    account_number: NotRequired[str]
    r"""The account number associated with the contract."""
    additional_addresses: NotRequired[str]
    r"""Any additional addresses associated with the contract."""
    balance: NotRequired[int]
    r"""Current balance of the contract in cents. (precision 2)"""
    balance_currency: NotRequired[str]
    r"""Currency code in ISO 4217 format"""
    billing_address: NotRequired[str]
    r"""The billing address associated with the contract."""
    billing_due_day: NotRequired[int]
    r"""Defines the day of the month in which the installments are due."""
    billing_duration_amount: NotRequired[float]
    r"""The duration of the billing period."""
    billing_period: NotRequired[BillingPeriod]
    r"""The billing period associated with the contract."""
    branch: NotRequired[Branch]
    r"""The branch associated with the contract."""
    contract_name: NotRequired[str]
    r"""The name of the contract."""
    contract_number: NotRequired[str]
    r"""The unique identifier of the contract."""
    delivery_address: NotRequired[str]
    r"""The delivery address associated with the contract."""
    description: NotRequired[str]
    r"""A brief description of the contract."""
    installment_amount: NotRequired[int]
    r"""Set amount for installments in cents. (precision 2)"""
    notice_time_amount: NotRequired[float]
    r"""The amount of notice required for termination of the contract."""
    notice_time_unit: NotRequired[NoticeTimeUnit]
    r"""The unit of time for the notice period."""
    renewal_duration_amount: NotRequired[float]
    r"""The duration of the renewal period."""
    renewal_duration_unit: NotRequired[RenewalDurationUnit]
    r"""The unit of time for the renewal period."""
    start_date: NotRequired[str]
    r"""The start date of the contract."""
    status: NotRequired[Status]
    r"""The status of the contract."""
    termination_date: NotRequired[str]
    r"""The date on which the contract was terminated."""
    termination_reason: NotRequired[str]
    r"""The reason for the termination of the contract."""
    

class Contract(BaseModel):
    r"""The contract entity"""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    created_at: Annotated[datetime, pydantic.Field(alias="_created_at")]
    r"""Creation timestamp of the entity"""
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""Entity ID"""
    org: Annotated[str, pydantic.Field(alias="_org")]
    r"""Organization ID the entity belongs to"""
    title: Annotated[str, pydantic.Field(alias="_title")]
    r"""Title of the entity"""
    updated_at: Annotated[datetime, pydantic.Field(alias="_updated_at")]
    r"""Last update timestamp of the entity"""
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    r"""Array of entity tags"""
    account_number: Optional[str] = None
    r"""The account number associated with the contract."""
    additional_addresses: Optional[str] = None
    r"""Any additional addresses associated with the contract."""
    balance: Optional[int] = None
    r"""Current balance of the contract in cents. (precision 2)"""
    balance_currency: Optional[str] = None
    r"""Currency code in ISO 4217 format"""
    billing_address: Optional[str] = None
    r"""The billing address associated with the contract."""
    billing_due_day: Optional[int] = None
    r"""Defines the day of the month in which the installments are due."""
    billing_duration_amount: Optional[float] = None
    r"""The duration of the billing period."""
    billing_period: Optional[BillingPeriod] = BillingPeriod.WEEKLY
    r"""The billing period associated with the contract."""
    branch: Optional[Branch] = None
    r"""The branch associated with the contract."""
    contract_name: Optional[str] = None
    r"""The name of the contract."""
    contract_number: Optional[str] = None
    r"""The unique identifier of the contract."""
    delivery_address: Optional[str] = None
    r"""The delivery address associated with the contract."""
    description: Optional[str] = None
    r"""A brief description of the contract."""
    installment_amount: Optional[int] = None
    r"""Set amount for installments in cents. (precision 2)"""
    notice_time_amount: Optional[float] = None
    r"""The amount of notice required for termination of the contract."""
    notice_time_unit: Optional[NoticeTimeUnit] = NoticeTimeUnit.MONTHS
    r"""The unit of time for the notice period."""
    renewal_duration_amount: Optional[float] = None
    r"""The duration of the renewal period."""
    renewal_duration_unit: Optional[RenewalDurationUnit] = RenewalDurationUnit.MONTHS
    r"""The unit of time for the renewal period."""
    start_date: Optional[str] = None
    r"""The start date of the contract."""
    status: Optional[Status] = Status.DRAFT
    r"""The status of the contract."""
    termination_date: Optional[str] = None
    r"""The date on which the contract was terminated."""
    termination_reason: Optional[str] = None
    r"""The reason for the termination of the contract."""
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    
