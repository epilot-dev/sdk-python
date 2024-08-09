"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .origin import Origin
from .upsertportalwidget import UpsertPortalWidget, UpsertPortalWidgetTypedDict
from epilot_customer_portal.types import BaseModel
from epilot_customer_portal.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class UpsertPortalWidgetRequestTypedDict(TypedDict):
    upsert_portal_widget: UpsertPortalWidgetTypedDict
    r"""Portal widgets payload"""
    origin: Origin
    r"""Origin of the portal"""
    

class UpsertPortalWidgetRequest(BaseModel):
    upsert_portal_widget: Annotated[UpsertPortalWidget, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    r"""Portal widgets payload"""
    origin: Annotated[Origin, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    r"""Origin of the portal"""
    
