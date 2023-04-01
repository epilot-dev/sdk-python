"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations

class Export:
    r"""Export and Import entities via files"""
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
        
    def export_entities(self, request: operations.ExportEntitiesRequest) -> operations.ExportEntitiesResponse:
        r"""exportEntities
        create export file of entities
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity:export'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "entity_search_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ExportEntitiesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ExportEntitiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def import_entities(self, request: operations.ImportEntitiesRequest) -> operations.ImportEntitiesResponse:
        r"""importEntities
        import entity data from
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity:import'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "entity_import_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ImportEntitiesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ImportEntitiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    