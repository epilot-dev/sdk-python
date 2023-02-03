import dataclasses
from typing import Optional
from ..shared import retryreq as shared_retryreq


@dataclasses.dataclass
class RetriggerActionPathParams:
    action_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'action_id', 'style': 'simple', 'explode': False }})
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'execution_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetriggerActionRequest:
    path_params: RetriggerActionPathParams = dataclasses.field()
    request: Optional[shared_retryreq.RetryReq] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RetriggerActionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
