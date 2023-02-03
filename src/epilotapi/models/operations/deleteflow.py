import dataclasses
from typing import Optional
from ..shared import automationflow as shared_automationflow


@dataclasses.dataclass
class DeleteFlowPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flow_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteFlowRequest:
    path_params: DeleteFlowPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    
