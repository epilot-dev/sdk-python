import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Any, Optional

class Relations:
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

    
    def add_relations(self, request: operations.AddRelationsRequest) -> operations.AddRelationsResponse:
        r"""addRelations
        Relates one or more entities to parent entity by adding items to a relation attribute
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}/relations", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.AddRelationsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.RelationItem])
                res.relation_item = out

        return res

    
    def delete_relation(self, request: operations.DeleteRelationRequest) -> operations.DeleteRelationResponse:
        r"""deleteRelation
        Removes relation between two entities
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}/relations/{attribute}/{entity_id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("DELETE", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteRelationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def get_relations(self, request: operations.GetRelationsRequest) -> operations.GetRelationsResponse:
        r"""getRelations
        Returns 1st level direct relations for an entity.
        
        You can control whether to return the full entity or just the relation item with the `?hydrate` query param.
        
        Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}/relations", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetRelationsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[Any]])
                res.get_relations_resp = out

        return res

    
    def update_relation(self, request: operations.UpdateRelationRequest) -> operations.UpdateRelationResponse:
        r"""updateRelation
        Updates an existing relation between two entities.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}/relations/{attribute}/{entity_id}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateRelationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.RelationItem])
                res.relation_item = out

        return res

    