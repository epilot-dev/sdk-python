"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclasses.dataclass
class OperationObjectNodeUniq:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperationObjectNode:
    r"""Mapping operation nodes are either primitive values or operation node objects"""
    append: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_append'), 'exclude': lambda f: f is None }})
    r"""Append to array"""
    copy: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_copy'), 'exclude': lambda f: f is None }})
    r"""Copy JSONPath value from source entity context"""
    set: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_set'), 'exclude': lambda f: f is None }})
    uniq: Optional[Union[bool, List[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_uniq'), 'exclude': lambda f: f is None }})
    r"""Unique array"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
