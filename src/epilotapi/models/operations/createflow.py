from __future__ import annotations
import dataclasses
from ..shared import automationflow as shared_automationflow
from typing import Optional


@dataclasses.dataclass
class CreateFlowRequest:
    request: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    