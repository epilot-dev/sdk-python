"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_customer_portal.types import BaseModel
from typing import Dict, TypedDict


class ContactExistsRequestTypedDict(TypedDict):
    org_id: str
    r"""ID of the organization"""
    registration_identifiers: Dict[str, Dict[str, str]]
    r"""Identifier-value pairs per schema to identify a contact of a portal user during the resgistration"""
    

class ContactExistsRequest(BaseModel):
    org_id: str
    r"""ID of the organization"""
    registration_identifiers: Dict[str, Dict[str, str]]
    r"""Identifier-value pairs per schema to identify a contact of a portal user during the resgistration"""
    
