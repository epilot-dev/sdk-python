"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityitem import EntityItem, EntityItemTypedDict
from .file import File, FileTypedDict
from .journeyactions import JourneyActions, JourneyActionsTypedDict
from .opportunity import Opportunity, OpportunityTypedDict
from .order import Order, OrderTypedDict
from epilot_customer_portal.types import BaseModel
from epilot_customer_portal.utils import FieldMetadata, PathParamMetadata
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetOpportunityRequestTypedDict(TypedDict):
    id: str
    r"""The ID of opportunity"""
    

class GetOpportunityRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of opportunity"""
    

class GetOpportunityResponseBodyTypedDict(TypedDict):
    r"""The returned opportunities"""
    
    entity: NotRequired[OpportunityTypedDict]
    r"""The opportunity entity"""
    files: NotRequired[List[FileTypedDict]]
    r"""The related files of the requested opportunity"""
    journey_actions: NotRequired[List[JourneyActionsTypedDict]]
    orders: NotRequired[List[OrderTypedDict]]
    r"""The related orders of the requested opportunity"""
    relations: NotRequired[List[EntityItemTypedDict]]
    r"""The related entities of the requested opportunity"""
    workflow: NotRequired[List[Dict[str, Any]]]
    r"""The related workflows of the requested opportunity"""
    

class GetOpportunityResponseBody(BaseModel):
    r"""The returned opportunities"""
    
    entity: Optional[Opportunity] = None
    r"""The opportunity entity"""
    files: Optional[List[File]] = None
    r"""The related files of the requested opportunity"""
    journey_actions: Optional[List[JourneyActions]] = None
    orders: Optional[List[Order]] = None
    r"""The related orders of the requested opportunity"""
    relations: Optional[List[EntityItem]] = None
    r"""The related entities of the requested opportunity"""
    workflow: Optional[List[Dict[str, Any]]] = None
    r"""The related workflows of the requested opportunity"""
    
