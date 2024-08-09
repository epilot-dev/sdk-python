"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_message.types import BaseModel
from epilot_message.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AssignUsersRequestBodyTypedDict(TypedDict):
    r"""User IDs of users assigned to thread"""
    
    assigned_to: NotRequired[List[str]]
    r"""IDs of users assigned to thread"""
    

class AssignUsersRequestBody(BaseModel):
    r"""User IDs of users assigned to thread"""
    
    assigned_to: Optional[List[str]] = None
    r"""IDs of users assigned to thread"""
    

class AssignUsersRequestTypedDict(TypedDict):
    request_body: AssignUsersRequestBodyTypedDict
    id: str
    r"""Thread ID"""
    

class AssignUsersRequest(BaseModel):
    request_body: Annotated[AssignUsersRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Thread ID"""
    