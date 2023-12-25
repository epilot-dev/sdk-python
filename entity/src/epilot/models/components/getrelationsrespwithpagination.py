"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .relationentity import RelationEntity
from .relationitem import RelationItem
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRelationsRespWithPagination:
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    relations: Optional[List[Union[RelationItem, RelationEntity]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relations'), 'exclude': lambda f: f is None }})
    
