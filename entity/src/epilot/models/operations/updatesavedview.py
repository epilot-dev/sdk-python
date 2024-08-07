"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import savedview as shared_savedview
from ..shared import savedviewitem as shared_savedviewitem
from typing import Optional


@dataclasses.dataclass
class UpdateSavedViewRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""View id"""
    saved_view: Optional[shared_savedview.SavedView] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateSavedViewResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    saved_view_item: Optional[shared_savedviewitem.SavedViewItem] = dataclasses.field(default=None)
    r"""Success"""
    

