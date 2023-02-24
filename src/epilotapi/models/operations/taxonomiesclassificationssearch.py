from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclasses.dataclass
class TaxonomiesClassificationsSearchQueryParams:
    taxonomy_slug: str = dataclasses.field(metadata={'query_param': { 'field_name': 'taxonomySlug', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequestBody:
    classification_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classificationIds'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequest:
    query_params: TaxonomiesClassificationsSearchQueryParams = dataclasses.field()
    request: Optional[TaxonomiesClassificationsSearchRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomiesClassificationsSearch200ApplicationJSON:
    results: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    taxonomies_classifications_search_200_application_json_object: Optional[TaxonomiesClassificationsSearch200ApplicationJSON] = dataclasses.field(default=None)
    