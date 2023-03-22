"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Schemas:
    r"""Model Entities"""
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
        
    def delete_schema(self, request: operations.DeleteSchemaRequest) -> operations.DeleteSchemaResponse:
        r"""deleteSchema
        Delete a schema, or a specific version of a schema
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteSchemaRequest, base_url, '/v1/entity/schemas/{slug}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteSchemaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def get_schema(self, request: operations.GetSchemaRequest) -> operations.GetSchemaResponse:
        r"""getSchema
        By default gets the latest version of the Schema and to get the specific version of schema pass the id.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSchemaRequest, base_url, '/v1/entity/schemas/{slug}', request)
        
        query_params = utils.get_query_params(operations.GetSchemaRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSchemaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EntitySchemaItem])
                res.entity_schema_item = out

        return res

    def get_schema_versions(self, request: operations.GetSchemaVersionsRequest) -> operations.GetSchemaVersionsResponse:
        r"""getSchemaVersions
        Get all versions of this schema ordered by the latest versions including drafts.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSchemaVersionsRequest, base_url, '/v1/entity/schemas/{slug}/versions', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSchemaVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSchemaVersions200ApplicationJSON])
                res.get_schema_versions_200_application_json_object = out

        return res

    def list_schema_blueprints(self) -> operations.ListSchemaBlueprintsResponse:
        r"""listSchemaBlueprints
        List canonical versions of all available schemas
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity/schemas/blueprints'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListSchemaBlueprintsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListSchemaBlueprints200ApplicationJSON])
                res.list_schema_blueprints_200_application_json_object = out

        return res

    def list_schemas(self, request: operations.ListSchemasRequest) -> operations.ListSchemasResponse:
        r"""listSchemas
        Get the latest versions of all schemas
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity/schemas'
        
        query_params = utils.get_query_params(operations.ListSchemasRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListSchemasResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListSchemas200ApplicationJSON])
                res.list_schemas_200_application_json_object = out

        return res

    def list_taxonomy_classifications_for_schema(self, request: operations.ListTaxonomyClassificationsForSchemaRequest) -> operations.ListTaxonomyClassificationsForSchemaResponse:
        r"""listTaxonomyClassificationsForSchema
        List taxonomy classifications for a given schema
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListTaxonomyClassificationsForSchemaRequest, base_url, '/v1/entity/schemas/{slug}/taxonomy/{taxonomySlug}', request)
        
        query_params = utils.get_query_params(operations.ListTaxonomyClassificationsForSchemaRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListTaxonomyClassificationsForSchemaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListTaxonomyClassificationsForSchema200ApplicationJSON])
                res.list_taxonomy_classifications_for_schema_200_application_json_object = out

        return res

    def put_schema(self, request: operations.PutSchemaRequest) -> operations.PutSchemaResponse:
        r"""putSchema
        Create or update a schema with a new version
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutSchemaRequest, base_url, '/v1/entity/schemas/{slug}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "entity_schema", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.PutSchemaRequest, request)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutSchemaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EntitySchemaItem])
                res.entity_schema_item = out

        return res

    