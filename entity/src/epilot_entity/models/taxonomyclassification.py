"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from epilot_entity.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class TaxonomyClassificationTypedDict(TypedDict):
    name: str
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    parents: NotRequired[List[str]]
    slug: NotRequired[str]
    r"""URL-friendly identifier for the classification"""
    updated_at: NotRequired[datetime]
    

class TaxonomyClassification(BaseModel):
    name: str
    created_at: Optional[datetime] = None
    id: Optional[str] = None
    parents: Optional[List[str]] = None
    slug: Optional[str] = None
    r"""URL-friendly identifier for the classification"""
    updated_at: Optional[datetime] = None
    
