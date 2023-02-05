import dataclasses
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclasses.dataclass
class ListTaxonomyClassificationsForSchemaPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListTaxonomyClassificationsForSchemaQueryParams:
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListTaxonomyClassificationsForSchemaRequest:
    path_params: ListTaxonomyClassificationsForSchemaPathParams = dataclasses.field()
    query_params: ListTaxonomyClassificationsForSchemaQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class ListTaxonomyClassificationsForSchema200ApplicationJSON:
    results: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListTaxonomyClassificationsForSchemaResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_taxonomy_classifications_for_schema_200_application_json_object: Optional[ListTaxonomyClassificationsForSchema200ApplicationJSON] = dataclasses.field(default=None)
    