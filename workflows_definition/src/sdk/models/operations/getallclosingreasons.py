"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import closingreasons as components_closingreasons
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetAllClosingReasonsRequest:
    include_inactive: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeInactive', 'style': 'form', 'explode': True }})
    r"""Filter Closing Reasons by status like active inactiv"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllClosingReasonsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    closing_reasons: Optional[components_closingreasons.ClosingReasons] = dataclasses.field(default=None)
    r"""Returns the entire catalog of closing reasons per organization"""
    

