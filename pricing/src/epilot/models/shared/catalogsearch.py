"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import availabilityfilters as shared_availabilityfilters
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogSearch:
    r"""A catalog search payload"""
    
    q: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('q') }})
    r"""The query to perform using lucene query syntax."""  
    availability: Optional[shared_availabilityfilters.AvailabilityFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availability'), 'exclude': lambda f: f is None }})
    r"""Availability filters dimensions"""  
    from_: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    r"""The index from which to query, used for pagination purposes. Defaults to 0"""  
    hydrate: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hydrate'), 'exclude': lambda f: f is None }})
    r"""When true, enables entity hydration to resolve nested $relation references in-place."""  
    size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""The max size of the response, defaults to 2000."""  
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    r"""The sort expression to sort the results."""  
    