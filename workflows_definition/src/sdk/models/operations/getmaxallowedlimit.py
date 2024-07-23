"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import maxallowedlimit as components_maxallowedlimit
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMaxAllowedLimitResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    max_allowed_limit: Optional[components_maxallowedlimit.MaxAllowedLimit] = dataclasses.field(default=None)
    r"""A combo of current number of workflows, and the max allowed number of workflows."""
    

