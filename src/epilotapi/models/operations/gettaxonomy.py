import dataclasses
from typing import Optional
from ..shared import taxonomy as shared_taxonomy


@dataclasses.dataclass
class GetTaxonomyPathParams:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTaxonomyRequest:
    path_params: GetTaxonomyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTaxonomyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    taxonomy: Optional[shared_taxonomy.Taxonomy] = dataclasses.field(default=None)
    
