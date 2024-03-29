"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Activity:
    r"""Entity Events"""
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
        
    def attach_activity(self, request: operations.AttachActivityRequest) -> operations.AttachActivityResponse:
        r"""attachActivity
        Attach existing activity to entity activity feeds
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.AttachActivityRequest, base_url, '/v1/entity/activity/{id}:attach', request)
        
        query_params = utils.get_query_params(operations.AttachActivityRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params)
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
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity/activity'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "activity", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateActivityRequest, request)
        
        client = self._security_client
        
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
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetActivityRequest, base_url, '/v1/entity/activity/{id}', request)
        
        query_params = utils.get_query_params(operations.GetActivityRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
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
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetEntityActivityFeedRequest, base_url, '/v1/entity/{slug}/{id}/activity', request)
        
        query_params = utils.get_query_params(operations.GetEntityActivityFeedRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEntityActivityFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEntityActivityFeed200ApplicationJSON])
                res.get_entity_activity_feed_200_application_json_object = out

        return res

    