"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import filterconditiononevent as shared_filterconditiononevent
from ..shared import orcondition as shared_orcondition
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrCondition:
    dollar_or: Optional[list[Union[OrCondition, dict[str, list[Union[str, shared_equalsignorecasecondition.EqualsIgnoreCaseCondition, shared_anythingbutcondition.AnythingButCondition, shared_numericcondition.NumericCondition, shared_existscondition.ExistsCondition, shared_prefixcondition.PrefixCondition, shared_suffixcondition.SuffixCondition]]]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$or'), 'exclude': lambda f: f is None }})
    

