"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_pricing.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class SearchProvidersParamsType(str, Enum):
    r"""The provider type (power or gas)"""
    POWER = "power"
    GAS = "gas"

class SearchProvidersParamsTypedDict(TypedDict):
    r"""A search providers payload"""
    
    postal_code: str
    r"""The postal code to search for providers"""
    type: SearchProvidersParamsType
    r"""The provider type (power or gas)"""
    city: NotRequired[Nullable[str]]
    r"""The city to search for providers"""
    street: NotRequired[Nullable[str]]
    r"""The street to search for providers"""
    street_number: NotRequired[Nullable[str]]
    r"""The street number to search for providers"""
    

class SearchProvidersParams(BaseModel):
    r"""A search providers payload"""
    
    postal_code: str
    r"""The postal code to search for providers"""
    type: SearchProvidersParamsType
    r"""The provider type (power or gas)"""
    city: OptionalNullable[str] = UNSET
    r"""The city to search for providers"""
    street: OptionalNullable[str] = UNSET
    r"""The street to search for providers"""
    street_number: OptionalNullable[str] = UNSET
    r"""The street number to search for providers"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["city", "street", "street_number"]
        nullable_fields = ["city", "street", "street_number"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
