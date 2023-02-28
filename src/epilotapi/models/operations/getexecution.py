from __future__ import annotations
import dataclasses
from ..shared import automationexecution as shared_automationexecution
from typing import Optional


@dataclasses.dataclass
class GetExecutionPathParams:
    execution_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'execution_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetExecutionRequest:
    path_params: GetExecutionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetExecutionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    automation_execution: Optional[shared_automationexecution.AutomationExecution] = dataclasses.field(default=None)
    