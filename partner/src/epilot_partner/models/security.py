"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_partner.types import BaseModel
from epilot_partner.utils import FieldMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SecurityTypedDict(TypedDict):
    as_organization: NotRequired[str]
    epilot_auth: NotRequired[str]
    

class Security(BaseModel):
    as_organization: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="apiKey", sub_type="header", field_name="x-ivy-org-id"))] = None
    epilot_auth: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    
