import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Optional

class Entities:
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

    
    def autocomplete(self, request: operations.AutocompleteRequest) -> operations.AutocompleteResponse:
        r"""autocomplete
        Autocomplete entity attributes
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity:autocomplete"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.AutocompleteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.Autocomplete200ApplicationJSON])
                res.autocomplete_200_application_json_object = out

        return res

    
    def create_entity(self, request: operations.CreateEntityRequest) -> operations.CreateEntityResponse:
        r"""createEntity
        Creates a new entity using a key.
        
        ## Activity
        
        If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityCreated`
        
        ## Relations
        
        To create a relation, store a property object that defines a `$relation` array.
        
        Example:
        
        ```json
        {
          \"contacts\": {
            \"$relation\": [
              { \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\" }
            ]
          }
        }
        ```
        
        The items in `$relation` support two properties:
        - `entity_id` - The ID of the entity to link
        - `_tags` - Tags or labels for the relation (optional)
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def delete_entity(self, request: operations.DeleteEntityRequest) -> operations.DeleteEntityResponse:
        r"""deleteEntity
        Deletes an Entity
        
        ## Activity
        
        If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityDeleted`
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("DELETE", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_entity(self, request: operations.GetEntityRequest) -> operations.GetEntityResponse:
        r"""getEntity
        Gets Entity and relations by id.
        
        ## Relations
        
        When `hydrate=true`, relation attributes are replaced in-place with nested entity values.
        
        Example:
        ```json
        {
          \"_id\": \"123\",
          \"name\": \"parent\",
          \"_tags\": [\"parent\"],
          \"contacts\": {
            \"$relation\": [
              { \"entity_id\": \"456\", \"_tags\": [\"primary\"] },
              { \"entity_id\": \"789\", \"_tags\": [\"secondary\"] },
            ]
          },
          \"addresses\": {
            \"$relation_ref\": [
              { \"entity_id\": \"123\", \"_tags\": [\"primary\"], \"path\": \"address.0\" },
              { \"entity_id\": \"234\", \"_tags\": [\"secondary\"], \"path\": \"address.0\" },
            ]
          }
        }
        ```
        
        Becomes:
        ```json
        {
          \"_id\": \"123\",
          \"name\": \"parent\",
          \"_tags\": [\"parent\"],
          \"contacts\": [
            {
              \"$relation\": { \"entity_id\": \"456\", \"_tags\": [\"primary\"] },
              \"_id\": \"456\",
              \"name\": \"child 1\",
              \"_tags\": [\"child\"]
            },
            {
              \"$relation\": { \"entity_id\": \"789\", \"_tags\": [\"secondary\"] },
              \"_id\": \"789\",
              \"name\": \"child 2\",
              \"_tags\": [\"child\"]
            }
          ],
          \"addresses\": [
            {
              \"$relation_ref\": { \"entity_id\": \"123\", \"_tags\": [\"primary\"], \"path\": \"address.0\" },
              \"_id\": \"123\",
              \"address\": \"address 1\",
              \"_tags\": [\"child\"]
            },
            {
              \"$relation_ref\": { \"entity_id\": \"234\", \"_tags\": [\"secondary\"], \"path\": \"address.0\" },
              \"_id\": \"234\",
              \"address\": \"address 2\",
              \"_tags\": [\"child\"]
            }
          ]
        }
        ```
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetEntity200ApplicationJSON])
                res.get_entity_200_application_json_object = out

        return res

    
    def search_entities(self, request: operations.SearchEntitiesRequest) -> operations.SearchEntitiesResponse:
        r"""searchEntities
        Search for entities. Supports ordering and pagination. Lucene query syntax supported for complex querying.
        
        Passing comma-separated `x-epilot-org-id` is supported for cross-org entity search.
        
        ## Relations
        
        When `hydrate=true`, relation attributes are replaced in-place with nested entity values.
        
        Example:
        ```json
        {
          \"_id\": \"123\",
          \"name\": \"parent\",
          \"_tags\": [\"parent\"],
          \"contacts\": {
            \"$relation\": [
              { \"entity_id\": \"456\", \"_tags\": [\"primary\"] },
              { \"entity_id\": \"789\", \"_tags\": [\"secondary\"] },
            ]
          },
          \"addresses\": {
            \"$relation_ref\": [
              { \"entity_id\": \"123\", \"_tags\": [\"primary\"], \"path\": \"address.0\" },
              { \"entity_id\": \"234\", \"_tags\": [\"secondary\"], \"path\": \"address.0\" },
            ]
          }
        }
        ```
        
        Becomes:
        ```json
        {
          \"_id\": \"123\",
          \"name\": \"parent\",
          \"_tags\": [\"parent\"],
          \"contacts\": [
            {
              \"$relation\": { \"entity_id\": \"456\", \"_tags\": [\"primary\"] },
              \"_id\": \"456\",
              \"name\": \"child 1\",
              \"_tags\": [\"child\"]
            },
            {
              \"$relation\": { \"entity_id\": \"789\", \"_tags\": [\"secondary\"] },
              \"_id\": \"789\",
              \"name\": \"child 2\",
              \"_tags\": [\"child\"]
            }
          ],
          \"addresses\": [
            {
              \"$relation_ref\": { \"entity_id\": \"123\", \"_tags\": [\"primary\"], \"path\": \"address.0\" },
              \"_id\": \"123\",
              \"address\": \"address 1\",
              \"_tags\": [\"child\"]
            },
            {
              \"$relation_ref\": { \"entity_id\": \"234\", \"_tags\": [\"secondary\"], \"path\": \"address.0\" },
              \"_id\": \"234\",
              \"address\": \"address 2\",
              \"_tags\": [\"child\"]
            }
          ]
        }
        ```
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity:search"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SearchEntitiesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EntitySearchResults])
                res.entity_search_results = out
            if utils.match_content_type(content_type, "text/csv"):
                res.search_entities_200_text_csv_string = r.content

        return res

    
    def update_entity(self, request: operations.UpdateEntityRequest) -> operations.UpdateEntityResponse:
        r"""updateEntity
        Updates an Entity
        
        ## Activity
        
        If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityUpdated`
        
        ## Relations
        
        To create a relation, store a property that defines a `$relation` array.
        
        Example:
        
        ```json
        {
          \"contacts\": {
            \"$relation\": [
              { \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\" }
            ]
          }
        }
        ```
        
        The items in `$relation` support two properties:
        - `entity_id` - The ID of the entity to link
        - `_tags` - Tags or labels for the relation (optional)
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("PUT", url, params=query_params, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def upsert_entity(self, request: operations.UpsertEntityRequest) -> operations.UpsertEntityResponse:
        r"""upsertEntity
        Create or update an entity using `unique_key`
        
        - If no entities are matched, a new entity is created.
        - If exactly one entity is matched, a `PATCH`-style update is applied to the existing entity.
        - If more than one entity is matched a `409` Error is returned
        
        ## Activity
        
        If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityCreated` or `EntityUpdated`
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}:upsert", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("PATCH", url, params=query_params, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpsertEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.entity_item = out
        elif r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.entity_item = out
        elif r.status_code == 409:
            pass

        return res

    