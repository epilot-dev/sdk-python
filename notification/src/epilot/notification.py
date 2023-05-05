"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations
from typing import Any, Optional

class Notification:
    r"""Notification"""
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
        
    
    def create_notification(self, request: dict[str, Any]) -> operations.CreateNotificationResponse:
        r"""createNotification
        Create a message that can be displayed in the notification panel.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/notification/notifications'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateNotificationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def get_notification(self, request: operations.GetNotificationRequest) -> operations.GetNotificationResponse:
        r"""getNotification
        Get the details of a single notification.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetNotificationRequest, base_url, '/v1/notification/notifications/{id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetNotificationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.notification_item = out

        return res

    
    def get_notifications(self, request: operations.GetNotificationsRequest) -> operations.GetNotificationsResponse:
        r"""getNotifications
        Get notifications
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/notification/notifications'
        
        query_params = utils.get_query_params(operations.GetNotificationsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetNotificationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetNotifications200ApplicationJSON])
                res.get_notifications_200_application_json_object = out

        return res

    
    def get_total_unread(self) -> operations.GetTotalUnreadResponse:
        r"""getTotalUnread
        Get total unread
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/notification/unreads'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTotalUnreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'text/plain'):
                res.get_total_unread_200_text_plain_number = http_res.content

        return res

    
    def mark_all_as_read(self) -> operations.MarkAllAsReadResponse:
        r"""markAllAsRead
        Mark all as read
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/notification/notifications/mark'
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkAllAsReadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def mark_as_read(self, request: operations.MarkAsReadRequest) -> operations.MarkAsReadResponse:
        r"""markAsRead
        Mark as read
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.MarkAsReadRequest, base_url, '/v1/notification/notifications/{id}/mark', request)
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkAsReadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    