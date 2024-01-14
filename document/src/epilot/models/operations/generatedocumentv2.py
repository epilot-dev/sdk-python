"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import documentgenerationv2request as components_documentgenerationv2request
from ...models.components import documentgenerationv2response as components_documentgenerationv2response
from enum import Enum
from typing import Optional

class Mode(str, Enum):
    r"""Type of mode used for document generation flow.
    Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.
    Full - Goes through all the steps for the full generation of final document
    """
    PARTIAL_GENERATION = 'partial_generation'
    FULL_GENERATION = 'full_generation'


@dataclasses.dataclass
class GenerateDocumentV2Request:
    document_generation_v2_request: Optional[components_documentgenerationv2request.DocumentGenerationV2Request] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    r"""Job ID for tracking the status of document generation action"""
    mode: Optional[Mode] = dataclasses.field(default=Mode.undefined, metadata={'query_param': { 'field_name': 'mode', 'style': 'form', 'explode': True }})
    r"""Type of mode used for document generation flow.
    Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.
    Full - Goes through all the steps for the full generation of final document
    """
    



@dataclasses.dataclass
class GenerateDocumentV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    document_generation_v2_response: Optional[components_documentgenerationv2response.DocumentGenerationV2Response] = dataclasses.field(default=None)
    r"""Generated document output"""
    

