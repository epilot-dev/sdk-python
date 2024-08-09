"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .file import File, FileTypedDict
from epilot_customer_portal.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SaveEntityFileResponseBodyTypedDict(TypedDict):
    r"""The files have been saved to the entitiy successfully."""
    
    created_files: NotRequired[List[FileTypedDict]]
    

class SaveEntityFileResponseBody(BaseModel):
    r"""The files have been saved to the entitiy successfully."""
    
    created_files: Annotated[Optional[List[File]], pydantic.Field(alias="createdFiles")] = None
    
