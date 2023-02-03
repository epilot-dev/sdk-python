import requests
from typing import Optional
from epilotapi.models import shared, operations
from . import utils

class Activity:
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

    
    def attach_activity(self, request: operations.AttachActivityRequest) -> operations.AttachActivityResponse:
        r"""attachActivity
        Attach existing activity to entity activity feeds
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/activity/{id}:attach", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.AttachActivityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def create_activity(self, request: operations.CreateActivityRequest) -> operations.CreateActivityResponse:
        r"""createActivity
        Create an activity that can be displayed in activity feeds.
        
        - All activites are published as events on the event bus
        - Entity mutations are always part of an activity
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/activity"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateActivityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def get_activity(self, request: operations.GetActivityRequest) -> operations.GetActivityResponse:
        r"""getActivity
        Get activity by id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/activity/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetActivityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ActivityItem])
                res.activity_item = out

        return res

    
    def get_entity_activity_feed(self, request: operations.GetEntityActivityFeedRequest) -> operations.GetEntityActivityFeedResponse:
        r"""getEntityActivityFeed
        Get activity feed for an entity
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/{slug}/{id}/activity", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEntityActivityFeedResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetEntityActivityFeed200ApplicationJSON])
                res.get_entity_activity_feed_200_application_json_object = out

        return res

    