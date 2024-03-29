"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import lastevaluatedkey as shared_lastevaluatedkey
from ..shared import workflowexecutionslim as shared_workflowexecutionslim
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchExecutionsResp:
    r"""Success - filtered steps are returned"""
    
    executions: list[shared_workflowexecutionslim.WorkflowExecutionSlim] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executions') }})  
    last_evaluated_key: Optional[shared_lastevaluatedkey.LastEvaluatedKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastEvaluatedKey'), 'exclude': lambda f: f is None }})  
    