import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Optional

class Schemas:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def create_new_schema_version(self, request: operations.CreateNewSchemaVersionRequest) -> operations.CreateNewSchemaVersionResponse:
        r"""createNewSchemaVersion
        Create new version of the schema and default draft is false.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/schemas/{slug}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateNewSchemaVersionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EntitySchemaItem])
                res.entity_schema_item = out

        return res

    
    def delete_schema_by_id(self, request: operations.DeleteSchemaByIDRequest) -> operations.DeleteSchemaByIDResponse:
        r"""deleteSchemaById
        Delete schema by Id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/schemas/{slug}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("DELETE", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteSchemaByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def get_schema(self, request: operations.GetSchemaRequest) -> operations.GetSchemaResponse:
        r"""getSchema
        By default gets the latest version of the Schema and to get the specific version of schema pass the id.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/schemas/{slug}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EntitySchemaItem])
                res.entity_schema_item = out

        return res

    
    def get_schema_versions(self, request: operations.GetSchemaVersionsRequest) -> operations.GetSchemaVersionsResponse:
        r"""getSchemaVersions
        Get all versions of this schema ordered by the latest versions including drafts.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/schemas/{slug}/versions", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaVersionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSchemaVersions200ApplicationJSON])
                res.get_schema_versions_200_application_json_object = out

        return res

    
    def list_schema_blueprints(self) -> operations.ListSchemaBlueprintsResponse:
        r"""listSchemaBlueprints
        List canonical versions of all available schemas
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/schemas/blueprints"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSchemaBlueprintsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSchemaBlueprints200ApplicationJSON])
                res.list_schema_blueprints_200_application_json_object = out

        return res

    
    def list_schemas(self, request: operations.ListSchemasRequest) -> operations.ListSchemasResponse:
        r"""listSchemas
        Get the latest version of local schema
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/schemas"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSchemasResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSchemas200ApplicationJSON])
                res.list_schemas_200_application_json_object = out

        return res

    
    def list_taxonomy_classifications_for_schema(self, request: operations.ListTaxonomyClassificationsForSchemaRequest) -> operations.ListTaxonomyClassificationsForSchemaResponse:
        r"""listTaxonomyClassificationsForSchema
        List taxonomy classifications for a given schema
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/schemas/{slug}/taxonomy/{taxonomySlug}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListTaxonomyClassificationsForSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListTaxonomyClassificationsForSchema200ApplicationJSON])
                res.list_taxonomy_classifications_for_schema_200_application_json_object = out

        return res

    