"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityrelation import EntityRelation, EntityRelationTypedDict
from .file import File, FileTypedDict
from enum import Enum
from epilot_pricing.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CrossSellableProductsTypedDict(TypedDict):
    r"""Stores references to products that can be cross sold with the current product."""
    
    dollar_relation: NotRequired[List[EntityRelationTypedDict]]
    

class CrossSellableProducts(BaseModel):
    r"""Stores references to products that can be cross sold with the current product."""
    
    dollar_relation: Annotated[Optional[List[EntityRelation]], pydantic.Field(alias="$relation")] = None
    

class FeatureTypedDict(TypedDict):
    tags: NotRequired[List[str]]
    r"""An arbitrary set of tags attached to a feature"""
    feature: NotRequired[str]
    

class Feature(BaseModel):
    tags: Annotated[Optional[List[str]], pydantic.Field(alias="_tags")] = None
    r"""An arbitrary set of tags attached to a feature"""
    feature: Optional[str] = None
    

class PriceOptionsTypedDict(TypedDict):
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    
    dollar_relation: NotRequired[List[EntityRelationTypedDict]]
    

class PriceOptions(BaseModel):
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    
    dollar_relation: Annotated[Optional[List[EntityRelation]], pydantic.Field(alias="$relation")] = None
    

class ProductDownloadsTypedDict(TypedDict):
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    
    dollar_relation: NotRequired[List[EntityRelationTypedDict]]
    

class ProductDownloads(BaseModel):
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    
    dollar_relation: Annotated[Optional[List[EntityRelation]], pydantic.Field(alias="$relation")] = None
    

class ProductImagesTypedDict(TypedDict):
    r"""Stores references to a set of file images of the product"""
    
    dollar_relation: NotRequired[List[EntityRelationTypedDict]]
    

class ProductImages(BaseModel):
    r"""Stores references to a set of file images of the product"""
    
    dollar_relation: Annotated[Optional[List[EntityRelation]], pydantic.Field(alias="$relation")] = None
    

class ProductType(str, Enum):
    r"""The type of Product:

    | type | description |
    |----| ----|
    | `product` | Represents a physical good |
    | `service` | Represents a service or virtual product |

    """
    PRODUCT = "product"
    SERVICE = "service"

class ProductTypedDict(TypedDict):
    r"""The product entity"""
    
    availability_files: NotRequired[List[FileTypedDict]]
    r"""Stores references to the availability files that define where this product is available.
    These files are used when interacting with products via epilot Journeys, thought the AvailabilityCheck block.

    """
    created_at: NotRequired[str]
    r"""The product creation date"""
    id: NotRequired[str]
    r"""The product id"""
    org_id: NotRequired[str]
    r"""The organization id the product belongs to"""
    title: NotRequired[str]
    r"""The autogenerated product title"""
    updated_at: NotRequired[str]
    r"""The product last update date"""
    code: NotRequired[str]
    r"""The product code"""
    cross_sellable_products: NotRequired[CrossSellableProductsTypedDict]
    r"""Stores references to products that can be cross sold with the current product."""
    description: NotRequired[str]
    r"""The description for the product"""
    feature: NotRequired[List[FeatureTypedDict]]
    name: NotRequired[str]
    r"""The product main name"""
    price_options: NotRequired[PriceOptionsTypedDict]
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    product_downloads: NotRequired[ProductDownloadsTypedDict]
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    product_images: NotRequired[ProductImagesTypedDict]
    r"""Stores references to a set of file images of the product"""
    type: NotRequired[ProductType]
    r"""The type of Product:

    | type | description |
    |----| ----|
    | `product` | Represents a physical good |
    | `service` | Represents a service or virtual product |

    """
    

class Product(BaseModel):
    r"""The product entity"""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    availability_files: Annotated[Optional[List[File]], pydantic.Field(alias="_availability_files")] = None
    r"""Stores references to the availability files that define where this product is available.
    These files are used when interacting with products via epilot Journeys, thought the AvailabilityCheck block.

    """
    created_at: Annotated[Optional[str], pydantic.Field(alias="_created_at")] = None
    r"""The product creation date"""
    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""The product id"""
    org_id: Annotated[Optional[str], pydantic.Field(alias="_org_id")] = None
    r"""The organization id the product belongs to"""
    title: Annotated[Optional[str], pydantic.Field(alias="_title")] = None
    r"""The autogenerated product title"""
    updated_at: Annotated[Optional[str], pydantic.Field(alias="_updated_at")] = None
    r"""The product last update date"""
    code: Optional[str] = None
    r"""The product code"""
    cross_sellable_products: Optional[CrossSellableProducts] = None
    r"""Stores references to products that can be cross sold with the current product."""
    description: Optional[str] = None
    r"""The description for the product"""
    feature: Optional[List[Feature]] = None
    name: Optional[str] = None
    r"""The product main name"""
    price_options: Optional[PriceOptions] = None
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    product_downloads: Optional[ProductDownloads] = None
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    product_images: Optional[ProductImages] = None
    r"""Stores references to a set of file images of the product"""
    type: Optional[ProductType] = None
    r"""The type of Product:

    | type | description |
    |----| ----|
    | `product` | Represents a physical good |
    | `service` | Represents a service or virtual product |

    """
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    

class ProductInputTypedDict(TypedDict):
    r"""The product entity"""
    
    availability_files: NotRequired[List[FileTypedDict]]
    r"""Stores references to the availability files that define where this product is available.
    These files are used when interacting with products via epilot Journeys, thought the AvailabilityCheck block.

    """
    id: NotRequired[str]
    r"""The product id"""
    org_id: NotRequired[str]
    r"""The organization id the product belongs to"""
    title: NotRequired[str]
    r"""The autogenerated product title"""
    code: NotRequired[str]
    r"""The product code"""
    cross_sellable_products: NotRequired[CrossSellableProductsTypedDict]
    r"""Stores references to products that can be cross sold with the current product."""
    description: NotRequired[str]
    r"""The description for the product"""
    feature: NotRequired[List[FeatureTypedDict]]
    name: NotRequired[str]
    r"""The product main name"""
    price_options: NotRequired[PriceOptionsTypedDict]
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    product_downloads: NotRequired[ProductDownloadsTypedDict]
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    product_images: NotRequired[ProductImagesTypedDict]
    r"""Stores references to a set of file images of the product"""
    type: NotRequired[ProductType]
    r"""The type of Product:

    | type | description |
    |----| ----|
    | `product` | Represents a physical good |
    | `service` | Represents a service or virtual product |

    """
    

class ProductInput(BaseModel):
    r"""The product entity"""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    availability_files: Annotated[Optional[List[File]], pydantic.Field(alias="_availability_files")] = None
    r"""Stores references to the availability files that define where this product is available.
    These files are used when interacting with products via epilot Journeys, thought the AvailabilityCheck block.

    """
    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""The product id"""
    org_id: Annotated[Optional[str], pydantic.Field(alias="_org_id")] = None
    r"""The organization id the product belongs to"""
    title: Annotated[Optional[str], pydantic.Field(alias="_title")] = None
    r"""The autogenerated product title"""
    code: Optional[str] = None
    r"""The product code"""
    cross_sellable_products: Optional[CrossSellableProducts] = None
    r"""Stores references to products that can be cross sold with the current product."""
    description: Optional[str] = None
    r"""The description for the product"""
    feature: Optional[List[Feature]] = None
    name: Optional[str] = None
    r"""The product main name"""
    price_options: Optional[PriceOptions] = None
    r"""A set of [prices](/api/pricing#tag/simple_price_schema) or [composite prices](/api/pricing#tag/dynamic_price_schema) for the current product."""
    product_downloads: Optional[ProductDownloads] = None
    r"""Stores references to a set of files downloadable from the product.
    e.g: tech specifications, quality control sheets, privacy policy agreements

    """
    product_images: Optional[ProductImages] = None
    r"""Stores references to a set of file images of the product"""
    type: Optional[ProductType] = None
    r"""The type of Product:

    | type | description |
    |----| ----|
    | `product` | Represents a physical good |
    | `service` | Represents a service or virtual product |

    """
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    