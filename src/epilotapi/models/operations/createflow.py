import dataclasses
from typing import Optional
from ..shared import automationflow as shared_automationflow


@dataclasses.dataclass
class CreateFlowRequest:
    request: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_flow: Optional[shared_automationflow.AutomationFlow] = dataclasses.field(default=None)
    
