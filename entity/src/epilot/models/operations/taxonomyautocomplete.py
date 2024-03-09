"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import taxonomyclassification as components_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclasses.dataclass
class TaxonomyAutocompleteRequest:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    r"""Taxonomy slug"""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Input to autocomplete"""
    size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    r"""Minimum number of results to return"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomyAutocompleteResponseBody:
    r"""Taxonomy classifications"""
    results: Optional[List[components_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class TaxonomyAutocompleteResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[TaxonomyAutocompleteResponseBody] = dataclasses.field(default=None)
    r"""Taxonomy classifications"""
    

