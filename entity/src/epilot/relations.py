"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import errors, operations, shared
from typing import List, Optional, Union

class Relations:
    r"""Entity Relationships"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def add_relations(self, request: operations.AddRelationsRequest) -> operations.AddRelationsResponse:
        r"""addRelations
        Relates one or more entities to parent entity by adding items to a relation attribute
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.AddRelationsRequest, base_url, '/v1/entity/{slug}/{id}/relations', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.AddRelationsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddRelationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RelationItem])
                res.relation_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def delete_relation(self, request: operations.DeleteRelationRequest) -> operations.DeleteRelationResponse:
        r"""deleteRelation
        Removes relation between two entities
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteRelationRequest, base_url, '/v1/entity/{slug}/{id}/relations/{attribute}/{entity_id}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteRelationRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteRelationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def get_related_entities_count(self, request: operations.GetRelatedEntitiesCountRequest) -> operations.GetRelatedEntitiesCountResponse:
        r"""getRelatedEntitiesCount
        Returns the amount of unique related entities for an entity - includes direct and reverse relations.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetRelatedEntitiesCountRequest, base_url, '/v2/entity/{slug}/{id}/relations/count', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetRelatedEntitiesCountRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRelatedEntitiesCountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetRelatedEntitiesCount])
                res.get_related_entities_count = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_relations(self, request: operations.GetRelationsRequest) -> operations.GetRelationsResponse:
        r"""getRelations
        Returns 1st level direct relations for an entity.

        You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

        Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetRelationsRequest, base_url, '/v1/entity/{slug}/{id}/relations', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetRelationsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRelationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[Union[shared.RelationItem, shared.RelationEntity]]])
                res.get_relations_resp = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_relations_v2(self, request: operations.GetRelationsV2Request) -> operations.GetRelationsV2Response:
        r"""getRelationsV2
        Returns 1st level direct relations for an entity with pagination.

        You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

        Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetRelationsV2Request, base_url, '/v2/entity/{slug}/{id}/relations', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetRelationsV2Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRelationsV2Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetRelationsRespWithPagination])
                res.get_relations_resp_with_pagination = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_relations_v3(self, request: operations.GetRelationsV3Request) -> operations.GetRelationsV3Response:
        r"""getRelationsV3
        Returns 1st level direct relations for an entity with pagination.

        You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

        Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetRelationsV3Request, base_url, '/v3/entity/{slug}/{id}/relations', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetRelationsV3Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRelationsV3Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetRelationsRespWithPagination])
                res.get_relations_resp_with_pagination = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def update_relation(self, request: operations.UpdateRelationRequest) -> operations.UpdateRelationResponse:
        r"""updateRelation
        Updates an existing relation between two entities.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateRelationRequest, base_url, '/v1/entity/{slug}/{id}/relations/{attribute}/{entity_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateRelationRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateRelationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RelationItem])
                res.relation_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    