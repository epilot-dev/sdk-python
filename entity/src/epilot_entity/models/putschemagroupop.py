"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityschemagroupwithcompositeid import EntitySchemaGroupWithCompositeIDInput, EntitySchemaGroupWithCompositeIDInputTypedDict
from epilot_entity.types import BaseModel
from epilot_entity.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PutSchemaGroupRequestTypedDict(TypedDict):
    composite_id: str
    r"""Schema Slug and the Group ID"""
    entity_schema_group_with_composite_id: NotRequired[EntitySchemaGroupWithCompositeIDInputTypedDict]
    

class PutSchemaGroupRequest(BaseModel):
    composite_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Schema Slug and the Group ID"""
    entity_schema_group_with_composite_id: Annotated[Optional[EntitySchemaGroupWithCompositeIDInput], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
