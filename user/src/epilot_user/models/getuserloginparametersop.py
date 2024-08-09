"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .loginparameters import LoginParameters, LoginParametersTypedDict
from epilot_user.types import BaseModel
from epilot_user.utils import FieldMetadata, PathParamMetadata
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetUserLoginParametersRequestTypedDict(TypedDict):
    username: str
    r"""Username"""
    

class GetUserLoginParametersRequest(BaseModel):
    username: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Username"""
    

class GetUserLoginParametersResponseBodyTypedDict(TypedDict):
    r"""User"""
    
    login_parameters: NotRequired[List[LoginParametersTypedDict]]
    

class GetUserLoginParametersResponseBody(BaseModel):
    r"""User"""
    
    login_parameters: Optional[List[LoginParameters]] = None
    
