"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operationnode as shared_operationnode
from ..shared import operationobjectnode as shared_operationobjectnode
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MappingAttributeV2:
    operation: Union[shared_operationobjectnode.OperationObjectNode, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation') }})
    r"""Mapping operation nodes are either primitive values or operation node objects"""
    target: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target'), 'exclude': lambda f: f is None }})
    r"""Target JSON path for the attribute to set"""
    

