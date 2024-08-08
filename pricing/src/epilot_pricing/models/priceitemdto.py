"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .externalfeemapping import ExternalFeeMapping, ExternalFeeMappingTypedDict
from .externalfeemetadata import ExternalFeeMetadata, ExternalFeeMetadataTypedDict
from .metadata import MetaData, MetaDataTypedDict
from .price import Price, PriceTypedDict
from .priceinputmapping import PriceInputMapping, PriceInputMappingTypedDict
from .product import ProductInput, ProductInputTypedDict
from enum import Enum
from epilot_pricing.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PriceItemDtoBillingPeriod(str, Enum):
    r"""The price billing period."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    EVERY_QUARTER = "every_quarter"
    EVERY_6_MONTHS = "every_6_months"
    YEARLY = "yearly"

class PriceItemDtoPricingModel(str, Enum):
    r"""Describes how to compute the price per period. Either `per_unit`, `tiered_graduated` or `tiered_volume`.
    - `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
    - `tiered_graduated` indicates that the unit pricing will be computed using tiers attribute. The customer pays the price per unit in every range their purchase rises through.
    - `tiered_volume` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `tiered_flatfee` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `external_getag` indicates that the price is influenced by aquisition fees provided by GetAG.

    """
    PER_UNIT = "per_unit"
    TIERED_GRADUATED = "tiered_graduated"
    TIERED_VOLUME = "tiered_volume"
    TIERED_FLATFEE = "tiered_flatfee"
    EXTERNAL_GETAG = "external_getag"

class PriceItemDtoType(str, Enum):
    r"""One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."""
    ONE_TIME = "one_time"
    RECURRING = "recurring"

class PriceItemDtoTypedDict(TypedDict):
    r"""Represents a price input to the pricing library."""
    
    pricing_model: PriceItemDtoPricingModel
    r"""Describes how to compute the price per period. Either `per_unit`, `tiered_graduated` or `tiered_volume`.
    - `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
    - `tiered_graduated` indicates that the unit pricing will be computed using tiers attribute. The customer pays the price per unit in every range their purchase rises through.
    - `tiered_volume` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `tiered_flatfee` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `external_getag` indicates that the price is influenced by aquisition fees provided by GetAG.

    """
    price: NotRequired[PriceTypedDict]
    r"""The snapshot of the price linked to the price item."""
    product: NotRequired[ProductInputTypedDict]
    r"""The snapshot of the product."""
    billing_period: NotRequired[PriceItemDtoBillingPeriod]
    r"""The price billing period."""
    description: NotRequired[str]
    r"""An arbitrary string attached to the price item. Often useful for displaying to users. Defaults to product name."""
    external_fees_mappings: NotRequired[List[ExternalFeeMappingTypedDict]]
    external_fees_metadata: NotRequired[ExternalFeeMetadataTypedDict]
    is_composite_price: NotRequired[bool]
    r"""The flag for prices that contain price components."""
    is_tax_inclusive: NotRequired[bool]
    r"""Specifies whether the price is considered `inclusive` of taxes or not."""
    metadata: NotRequired[List[MetaDataTypedDict]]
    r"""A set of key-value pairs used to store meta data information about an entity."""
    price_id: NotRequired[str]
    r"""The id of the price."""
    price_mappings: NotRequired[List[PriceInputMappingTypedDict]]
    product_id: NotRequired[str]
    r"""The id of the product."""
    quantity: NotRequired[int]
    r"""The quantity of products being purchased."""
    type: NotRequired[PriceItemDtoType]
    r"""One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."""
    unit_amount: NotRequired[int]
    r"""The unit amount value"""
    unit_amount_currency: NotRequired[str]
    r"""Three-letter ISO currency code, in lowercase. Must be a supported currency.
    ISO 4217 CURRENCY CODES as specified in the documentation: https://www.iso.org/iso-4217-currency-codes.html

    """
    unit_amount_decimal: NotRequired[str]
    r"""The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places."""
    unit_amount_gross: NotRequired[int]
    r"""The unit gross amount value."""
    

class PriceItemDto(BaseModel):
    r"""Represents a price input to the pricing library."""
    
    pricing_model: PriceItemDtoPricingModel
    r"""Describes how to compute the price per period. Either `per_unit`, `tiered_graduated` or `tiered_volume`.
    - `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
    - `tiered_graduated` indicates that the unit pricing will be computed using tiers attribute. The customer pays the price per unit in every range their purchase rises through.
    - `tiered_volume` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `tiered_flatfee` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
    - `external_getag` indicates that the price is influenced by aquisition fees provided by GetAG.

    """
    price: Annotated[Optional[Price], pydantic.Field(alias="_price")] = None
    r"""The snapshot of the price linked to the price item."""
    product: Annotated[Optional[ProductInput], pydantic.Field(alias="_product")] = None
    r"""The snapshot of the product."""
    billing_period: Optional[PriceItemDtoBillingPeriod] = None
    r"""The price billing period."""
    description: Optional[str] = None
    r"""An arbitrary string attached to the price item. Often useful for displaying to users. Defaults to product name."""
    external_fees_mappings: Optional[List[ExternalFeeMapping]] = None
    external_fees_metadata: Optional[ExternalFeeMetadata] = None
    is_composite_price: Optional[bool] = None
    r"""The flag for prices that contain price components."""
    is_tax_inclusive: Optional[bool] = None
    r"""Specifies whether the price is considered `inclusive` of taxes or not."""
    metadata: Optional[List[MetaData]] = None
    r"""A set of key-value pairs used to store meta data information about an entity."""
    price_id: Optional[str] = None
    r"""The id of the price."""
    price_mappings: Optional[List[PriceInputMapping]] = None
    product_id: Optional[str] = None
    r"""The id of the product."""
    quantity: Optional[int] = None
    r"""The quantity of products being purchased."""
    type: Optional[PriceItemDtoType] = None
    r"""One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."""
    unit_amount: Optional[int] = None
    r"""The unit amount value"""
    unit_amount_currency: Optional[str] = None
    r"""Three-letter ISO currency code, in lowercase. Must be a supported currency.
    ISO 4217 CURRENCY CODES as specified in the documentation: https://www.iso.org/iso-4217-currency-codes.html

    """
    unit_amount_decimal: Optional[str] = None
    r"""The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places."""
    unit_amount_gross: Optional[int] = None
    r"""The unit gross amount value."""
    
