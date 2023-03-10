from __future__ import annotations
import dataclasses
from ..shared import automationflow as shared_automationflow
from typing import Optional


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
    