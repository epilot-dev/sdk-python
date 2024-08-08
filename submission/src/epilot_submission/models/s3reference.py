"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_submission.types import BaseModel
from typing import TypedDict


class S3ReferenceTypedDict(TypedDict):
    r"""S3 Reference from File API"""
    
    bucket: str
    key: str
    

class S3Reference(BaseModel):
    r"""S3 Reference from File API"""
    
    bucket: str
    key: str
    
