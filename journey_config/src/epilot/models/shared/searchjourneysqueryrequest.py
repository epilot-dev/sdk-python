"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchJourneysQueryRequest:
    r"""Payload"""
    from_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    r"""The offset of the first result to return.
    See https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-from-size.html
    """
    q: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('q'), 'exclude': lambda f: f is None }})
    r"""Lucene query syntax
    See https://lucene.apache.org/core/2_9_4/queryparsersyntax.html ; https://www.elastic.co/guide/en/kibana/current/lucene-query.html
    """
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""The maximum number of results to return.
    See https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-from-size.html
    """
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    r"""The sort order. Follows Lucene syntax."""
    

