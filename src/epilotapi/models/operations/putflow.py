from __future__ import annotations
import dataclasses
from ..shared import automationflow as shared_automationflow
from typing import Optional


@dataclasses.dataclass
class PutFlowPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flow_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PutFlowRequest:
    path_params: PutFlowPathParams = dataclasses.field()
    request: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PutFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    