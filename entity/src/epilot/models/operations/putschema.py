"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import entityschema as components_entityschema
from ...models.components import entityschemaitem as components_entityschemaitem
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class PutSchemaRequest:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    entity_schema: Optional[components_entityschema.EntitySchema] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    draft: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'draft', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class PutSchemaResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    entity_schema_item: Optional[components_entityschemaitem.EntitySchemaItem] = dataclasses.field(default=None)
    r"""Success"""
    

