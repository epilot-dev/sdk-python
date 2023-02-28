from __future__ import annotations
import dataclasses
from ..shared import searchjourneysqueryrequest as shared_searchjourneysqueryrequest
from ..shared import searchjourneysresponse as shared_searchjourneysresponse
from typing import Optional


@dataclasses.dataclass
class SearchJourneysRequest:
    request: Optional[shared_searchjourneysqueryrequest.SearchJourneysQueryRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchJourneysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    search_journeys_response: Optional[shared_searchjourneysresponse.SearchJourneysResponse] = dataclasses.field(default=None)
    