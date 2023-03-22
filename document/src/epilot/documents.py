"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations
from typing import Optional

class Documents:
    r"""Document Generation"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def generate_document(self, request: operations.GenerateDocumentRequestBody) -> operations.GenerateDocumentResponse:
        r"""generateDocument
        Builds document generated from input document with variables.
        
        Supported input document types:
        - .docx
        
        Supported output document types:
        - .pdf
        
        Uses [Template Variables API](https://docs.epilot.io/api/template-variables) to replace variables in the document.
        
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/documents:generate'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GenerateDocumentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GenerateDocument200ApplicationJSON])
                res.generate_document_200_application_json_object = out

        return res

    