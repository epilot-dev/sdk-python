import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclasses.dataclass
class AutocompleteQueryParams:
    attribute: str = dataclasses.field(metadata={'query_param': { 'field_name': 'attribute', 'style': 'form', 'explode': True }})
    input: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'input', 'style': 'form', 'explode': True }})
    size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class AutocompleteRequest:
    query_params: AutocompleteQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class Autocomplete200ApplicationJSON:
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hits') }})
    results: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class AutocompleteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    autocomplete_200_application_json_object: Optional[Autocomplete200ApplicationJSON] = dataclasses.field(default=None)
    