"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import errors, operations
from typing import Optional

class Documents:
    r"""Document Generation"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def generate_document(self, request: operations.GenerateDocumentRequestBody) -> operations.GenerateDocumentResponse:
        r"""generateDocument
        Builds document generated from input document with variables.

        Supported input document types:
        - .docx

        Supported output document types:
        - .pdf

        Uses [Template Variables API](https://docs.epilot.io/api/template-variables) to replace variables in the document.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/documents:generate'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GenerateDocumentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GenerateDocumentResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def generate_document_v2(self, request_body: Optional[operations.GenerateDocumentV2RequestBody] = None, job_id: Optional[str] = None, mode: Optional[operations.Mode] = None) -> operations.GenerateDocumentV2Response:
        r"""generateDocumentV2
        Builds document generated from input document with variables.

        Supported input document types:
        - .docx

        Supported output document types:
        - .pdf
        - .docx but limited to only text based variables

        Uses [Template Variables API](https://docs.epilot.io/api/template-variables) to replace variables in the document.
        """
        request = operations.GenerateDocumentV2Request(
            request_body=request_body,
            job_id=job_id,
            mode=mode,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/documents:generate'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.GenerateDocumentV2Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GenerateDocumentV2Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GenerateDocumentV2ResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    