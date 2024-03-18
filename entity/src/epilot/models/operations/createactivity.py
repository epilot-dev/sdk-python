"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import activity as components_activity
from ...models.components import activityitem as components_activityitem
from ...models.components import httpmetadata as components_httpmetadata
from typing import List, Optional


@dataclasses.dataclass
class CreateActivityRequest:
    activity: Optional[components_activity.Activity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    entities: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entities', 'style': 'form', 'explode': False }})
    r"""Comma-separated list of entities which the activity primarily concerns"""
    



@dataclasses.dataclass
class CreateActivityResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    activity_item: Optional[components_activityitem.ActivityItem] = dataclasses.field(default=None)
    r"""Success"""
    

