import dataclasses
from typing import Optional
from ..shared import searchautomationsresp as shared_searchautomationsresp


@dataclasses.dataclass
class SearchFlowsQueryParams:
    from_: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'schema', 'style': 'form', 'explode': True }})
    size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    trigger_source_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'trigger_source_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SearchFlowsRequest:
    query_params: SearchFlowsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class SearchFlowsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    search_automations_resp: Optional[shared_searchautomationsresp.SearchAutomationsResp] = dataclasses.field(default=None)
    
