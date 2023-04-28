"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetNotificationRequest:
    
    id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})

    r"""Notification Id"""
    

@dataclasses.dataclass
class GetNotificationResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    notification_item: Optional[dict[str, Any]] = dataclasses.field(default=None)

    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    