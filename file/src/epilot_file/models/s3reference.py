"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_file.types import BaseModel
from typing import TypedDict


class S3ReferenceTypedDict(TypedDict):
    bucket: str
    key: str
    

class S3Reference(BaseModel):
    bucket: str
    key: str
    
