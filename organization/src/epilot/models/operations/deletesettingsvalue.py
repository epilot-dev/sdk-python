"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata


@dataclasses.dataclass
class DeleteSettingsValueRequest:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    r"""Organization setting key"""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""The Id of the organization."""
    



@dataclasses.dataclass
class DeleteSettingsValueResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    

