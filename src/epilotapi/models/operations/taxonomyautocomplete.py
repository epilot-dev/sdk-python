from __future__ import annotations
import dataclasses
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclasses.dataclass
class TaxonomyAutocompletePathParams:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TaxonomyAutocompleteQueryParams:
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TaxonomyAutocompleteRequest:
    path_params: TaxonomyAutocompletePathParams = dataclasses.field()
    query_params: TaxonomyAutocompleteQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomyAutocomplete200ApplicationJSON:
    results: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class TaxonomyAutocompleteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    taxonomy_autocomplete_200_application_json_object: Optional[TaxonomyAutocomplete200ApplicationJSON] = dataclasses.field(default=None)
    