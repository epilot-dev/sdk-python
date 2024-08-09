"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_file.types import BaseModel
from epilot_file.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PreviewFileRequestTypedDict(TypedDict):
    id: str
    h: NotRequired[int]
    r"""height"""
    version: NotRequired[int]
    r"""index of file version"""
    w: NotRequired[int]
    r"""width"""
    

class PreviewFileRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    h: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""height"""
    version: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""index of file version"""
    w: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""width"""
    
