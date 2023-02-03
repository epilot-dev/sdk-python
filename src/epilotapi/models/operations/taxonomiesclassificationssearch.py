import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclasses.dataclass
class TaxonomiesClassificationsSearchQueryParams:
    taxonomy_slug: str = dataclasses.field(metadata={'query_param': { 'field_name': 'taxonomySlug', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequestBody:
    classification_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classificationIds') }})
    

@dataclass_json
@dataclasses.dataclass
class TaxonomiesClassificationsSearch200ApplicationJSON:
    results: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequest:
    query_params: TaxonomiesClassificationsSearchQueryParams = dataclasses.field()
    request: Optional[TaxonomiesClassificationsSearchRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    taxonomies_classifications_search_200_application_json_object: Optional[TaxonomiesClassificationsSearch200ApplicationJSON] = dataclasses.field(default=None)
    
