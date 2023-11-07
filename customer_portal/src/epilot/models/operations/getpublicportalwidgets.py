"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import origin as components_origin
from ...models.components import upsertportalwidget as components_upsertportalwidget
from typing import Optional


@dataclasses.dataclass
class GetPublicPortalWidgetsRequest:
    org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'org_id', 'style': 'form', 'explode': True }})
    origin: components_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    



@dataclasses.dataclass
class GetPublicPortalWidgetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    upsert_portal_widget: Optional[components_upsertportalwidget.UpsertPortalWidget] = dataclasses.field(default=None)
    r"""Retrieved the portal public widgets successfully."""
    
