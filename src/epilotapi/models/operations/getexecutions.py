from __future__ import annotations
import dataclasses
from ..shared import getexecutionsresp as shared_getexecutionsresp
from typing import Optional


@dataclasses.dataclass
class GetExecutionsQueryParams:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entity_id', 'style': 'form', 'explode': True }})
    from_: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetExecutionsRequest:
    query_params: GetExecutionsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetExecutionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_executions_resp: Optional[shared_getexecutionsresp.GetExecutionsResp] = dataclasses.field(default=None)
    