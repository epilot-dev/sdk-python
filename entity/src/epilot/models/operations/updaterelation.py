"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import relationitem as shared_relationitem
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelationRequestBody:
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UpdateRelationRequest:
    attribute: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attribute', 'style': 'simple', 'explode': False }})
    r"""The attribute that express meaning"""
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    r"""The attribute that express meaning"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Entity id"""
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    request_body: Optional[UpdateRelationRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateRelationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    relation_item: Optional[shared_relationitem.RelationItem] = dataclasses.field(default=None)
    r"""Success"""
    

