"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import operations, shared
from typing import Optional

class Activity:
    r"""Entity Events"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def attach_activity(self, request: operations.AttachActivityRequest) -> operations.AttachActivityResponse:
        r"""attachActivity
        Attach existing activity to entity activity feeds
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.AttachActivityRequest, base_url, '/v1/entity/activity/{id}:attach', request)
        headers = {}
        query_params = utils.get_query_params(operations.AttachActivityRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AttachActivityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def create_activity(self, request: operations.CreateActivityRequest) -> operations.CreateActivityResponse:
        r"""createActivity
        Create an activity that can be displayed in activity feeds.

        - All activites are published as events on the event bus
        - Entity mutations are always part of an activity
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/entity/activity'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "activity", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateActivityRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateActivityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def get_activity(self, request: operations.GetActivityRequest) -> operations.GetActivityResponse:
        r"""getActivity
        Get activity by id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetActivityRequest, base_url, '/v1/entity/activity/{id}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetActivityRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetActivityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def get_entity_activity_feed(self, request: operations.GetEntityActivityFeedRequest) -> operations.GetEntityActivityFeedResponse:
        r"""getEntityActivityFeed
        Get activity feed for an entity
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetEntityActivityFeedRequest, base_url, '/v1/entity/{slug}/{id}/activity', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetEntityActivityFeedRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEntityActivityFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEntityActivityFeed200ApplicationJSON])
                res.get_entity_activity_feed_200_application_json_object = out

        return res

    