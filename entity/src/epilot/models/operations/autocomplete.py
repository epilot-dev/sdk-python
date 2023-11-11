"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclasses.dataclass
class AutocompleteRequest:
    attribute: str = dataclasses.field(metadata={'query_param': { 'field_name': 'attribute', 'style': 'form', 'explode': True }})
    r"""Autocomplete attribute"""
    input: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'input', 'style': 'form', 'explode': True }})
    r"""Input to autocomplete"""
    size: Optional[int] = dataclasses.field(default=10, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    r"""Maximum number of results to return"""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""Limit results to entity schema"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AutocompleteResponseBody:
    r"""Success"""
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    results: Optional[List[Union[str, bool, Dict[str, Any]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class AutocompleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[AutocompleteResponseBody] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

