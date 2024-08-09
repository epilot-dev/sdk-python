"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getrelationsresp import GetRelationsResp, GetRelationsRespTypedDict
from epilot_entity.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class GetRelationsRespWithPaginationTypedDict(TypedDict):
    hits: NotRequired[float]
    relations: NotRequired[List[GetRelationsRespTypedDict]]
    

class GetRelationsRespWithPagination(BaseModel):
    hits: Optional[float] = None
    relations: Optional[List[GetRelationsResp]] = None
    
