from __future__ import annotations
import dataclasses
from ..shared import automationexecution as shared_automationexecution
from ..shared import startexecutionrequest as shared_startexecutionrequest
from typing import Optional


@dataclasses.dataclass
class StartExecutionRequest:
    request: Optional[shared_startexecutionrequest.StartExecutionRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class StartExecutionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_execution: Optional[shared_automationexecution.AutomationExecution] = dataclasses.field(default=None)
    