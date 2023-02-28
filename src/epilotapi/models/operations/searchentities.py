from __future__ import annotations
import dataclasses
from ..shared import entitysearchparams as shared_entitysearchparams
from ..shared import entitysearchresults as shared_entitysearchresults
from typing import Optional


@dataclasses.dataclass
class SearchEntitiesRequest:
    request: Optional[shared_entitysearchparams.EntitySearchParams] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchEntitiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_search_results: Optional[shared_entitysearchresults.EntitySearchResults] = dataclasses.field(default=None)
    search_entities_200_text_csv_string: Optional[str] = dataclasses.field(default=None)
    