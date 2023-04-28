"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import s3reference as shared_s3reference
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class GenerateDocumentV2RequestBodyLanguageEnum(str, Enum):
    r"""Language to use"""
    EN = 'en'
    DE = 'de'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2RequestBodyTemplateDocument:
    r"""Input template document"""
    
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename'), 'exclude': lambda f: f is None }})

    r"""Document original filename"""
    s3ref: Optional[shared_s3reference.S3Reference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2RequestBodyVariablePayload:
    r"""Custom values for variables in the template. Takes the higher precedence than others."""
    
    additional_properties: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProperties'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2RequestBody:
    
    template_document: GenerateDocumentV2RequestBodyTemplateDocument = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template_document') }})

    r"""Input template document"""
    context_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_entity_id'), 'exclude': lambda f: f is None }})

    r"""Entity to use for variable context"""
    language: Optional[GenerateDocumentV2RequestBodyLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})

    r"""Language to use"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})

    r"""User Id for variable context"""
    variable_payload: Optional[GenerateDocumentV2RequestBodyVariablePayload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variable_payload'), 'exclude': lambda f: f is None }})

    r"""Custom values for variables in the template. Takes the higher precedence than others."""
    
class GenerateDocumentV2ModeEnum(str, Enum):
    r"""Type of mode used for document generation flow.
    Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.
    Full - Goes through all the steps for the full generation of final document
    """
    PARTIAL_GENERATION = 'partial_generation'
    FULL_GENERATION = 'full_generation'


@dataclasses.dataclass
class GenerateDocumentV2Request:
    
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})

    r"""Job ID for tracking the status of document generation action"""
    mode: Optional[GenerateDocumentV2ModeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'mode', 'style': 'form', 'explode': True }})

    r"""Type of mode used for document generation flow.
    Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.
    Full - Goes through all the steps for the full generation of final document
    """
    request_body: Optional[GenerateDocumentV2RequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSONDocxOutputOutputDocument:
    
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename'), 'exclude': lambda f: f is None }})

    r"""Generated document filename for DOCX"""
    s3ref: Optional[shared_s3reference.S3Reference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSONDocxOutput:
    
    output_document: Optional[GenerateDocumentV2200ApplicationJSONDocxOutputOutputDocument] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output_document'), 'exclude': lambda f: f is None }})

    preview_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preview_url'), 'exclude': lambda f: f is None }})

    r"""Pre-signed S3 GET URL for DOCX preview"""
    
class GenerateDocumentV2200ApplicationJSONJobStatusEnum(str, Enum):
    r"""Status of the job"""
    STARTED = 'STARTED'
    PROCESSING = 'PROCESSING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSONPdfOutputOutputDocument:
    
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename'), 'exclude': lambda f: f is None }})

    r"""Generated document filename for PDF"""
    s3ref: Optional[shared_s3reference.S3Reference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSONPdfOutput:
    
    output_document: Optional[GenerateDocumentV2200ApplicationJSONPdfOutputOutputDocument] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output_document'), 'exclude': lambda f: f is None }})

    preview_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preview_url'), 'exclude': lambda f: f is None }})

    r"""Pre-signed S3 GET URL for PDF preview"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSONVariablePayload:
    r"""List of variables and its corresponding replaced values from the document template"""
    
    additional_properties: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProperties'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateDocumentV2200ApplicationJSON:
    r"""Generated document output"""
    
    docx_output: Optional[GenerateDocumentV2200ApplicationJSONDocxOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('docx_output'), 'exclude': lambda f: f is None }})

    job_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_id'), 'exclude': lambda f: f is None }})

    job_status: Optional[GenerateDocumentV2200ApplicationJSONJobStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_status'), 'exclude': lambda f: f is None }})

    r"""Status of the job"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})

    r"""A message explaining the progress"""
    pdf_output: Optional[GenerateDocumentV2200ApplicationJSONPdfOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pdf_output'), 'exclude': lambda f: f is None }})

    variable_payload: Optional[GenerateDocumentV2200ApplicationJSONVariablePayload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variable_payload'), 'exclude': lambda f: f is None }})

    r"""List of variables and its corresponding replaced values from the document template"""
    

@dataclasses.dataclass
class GenerateDocumentV2Response:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    generate_document_v2_200_application_json_object: Optional[GenerateDocumentV2200ApplicationJSON] = dataclasses.field(default=None)

    r"""Generated document output"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    