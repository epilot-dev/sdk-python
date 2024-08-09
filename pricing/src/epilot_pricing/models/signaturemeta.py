"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_pricing.types import BaseModel
from typing import TypedDict


class SignatureMetaTypedDict(TypedDict):
    r"""Signature meta data payload"""
    
    signature: str
    r"""The signature hash of the payload"""
    timestamp: float
    r"""Timestamp of the signature"""
    

class SignatureMeta(BaseModel):
    r"""Signature meta data payload"""
    
    signature: str
    r"""The signature hash of the payload"""
    timestamp: float
    r"""Timestamp of the signature"""
    