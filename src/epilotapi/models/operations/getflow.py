import dataclasses
from typing import Optional
from ..shared import automationflow as shared_automationflow


@dataclasses.dataclass
class GetFlowPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flow_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetFlowRequest:
    path_params: GetFlowPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    
