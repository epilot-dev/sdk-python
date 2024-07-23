"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import templatetype as components_templatetype
from ...models.components import variableresult as components_variableresult
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchVariablesRequestBody:
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""Search string"""
    template_type: components_templatetype.TemplateType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template_type') }})
    entity_schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_schemas'), 'exclude': lambda f: f is None }})
    from_: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    lang: Optional[str] = dataclasses.field(default='de', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lang'), 'exclude': lambda f: f is None }})
    r"""2-letter language code (ISO 639-1)"""
    size: Optional[int] = dataclasses.field(default=25, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchVariablesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    classes: Optional[List[components_variableresult.VariableResult]] = dataclasses.field(default=None)
    r"""ok"""
    

