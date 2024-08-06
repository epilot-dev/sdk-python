"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_permissions.types import BaseModel
from epilot_permissions.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetRoleRequestTypedDict(TypedDict):
    role_id: str
    

class GetRoleRequest(BaseModel):
    role_id: Annotated[str, pydantic.Field(alias="roleId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    
