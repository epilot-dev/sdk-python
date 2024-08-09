"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .integrationid import IntegrationID
from .searchstreetsparams import SearchStreetsParams, SearchStreetsParamsTypedDict
from epilot_pricing.types import BaseModel
from epilot_pricing.utils import FieldMetadata, HeaderMetadata, PathParamMetadata, RequestMetadata, SecurityMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DollarSearchStreetsSecurityTypedDict(TypedDict):
    epilot_public_auth: NotRequired[str]
    

class DollarSearchStreetsSecurity(BaseModel):
    epilot_public_auth: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

class DollarSearchStreetsRequestTypedDict(TypedDict):
    search_streets_params: SearchStreetsParamsTypedDict
    x_epilot_org_id: str
    r"""The target Organization Id represented by the caller"""
    integration_id: IntegrationID
    r"""The integration identifier"""
    

class DollarSearchStreetsRequest(BaseModel):
    search_streets_params: Annotated[SearchStreetsParams, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    x_epilot_org_id: Annotated[str, pydantic.Field(alias="X-Epilot-Org-ID"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The target Organization Id represented by the caller"""
    integration_id: Annotated[IntegrationID, pydantic.Field(alias="integrationId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The integration identifier"""
    