"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GenerateQRcodeRequest:
    
    qrdata: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'qrdata', 'style': 'form', 'explode': True }})

    r"""Payload of the QR code"""
    

@dataclasses.dataclass
class GenerateQRcodeResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    