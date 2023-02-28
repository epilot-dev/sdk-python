from __future__ import annotations
import dataclasses
from ..shared import automationexecution as shared_automationexecution
from typing import Optional


@dataclasses.dataclass
class CancelExecutionPathParams:
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'execution_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CancelExecutionRequest:
    path_params: CancelExecutionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CancelExecutionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_execution: Optional[shared_automationexecution.AutomationExecution] = dataclasses.field(default=None)
    