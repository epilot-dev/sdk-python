"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Threads:
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
        
    def assign_thread(self, request: operations.AssignThreadRequest) -> operations.AssignThreadResponse:
        r"""assignThread
        Assign thread to entities
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.AssignThreadRequest, base_url, '/v1/message/threads/{id}/assign', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AssignThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def delete_thread(self, request: operations.DeleteThreadRequest) -> operations.DeleteThreadResponse:
        r"""deleteThread
        Immediately and permanently delete a thread. This operation cannot be undone.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteThreadRequest, base_url, '/v1/message/threads/{id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def mark_read_thread(self, request: operations.MarkReadThreadRequest) -> operations.MarkReadThreadResponse:
        r"""markReadThread
        Mark thread as read
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.MarkReadThreadRequest, base_url, '/v1/message/threads/{id}/read', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkReadThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def mark_unread_thread(self, request: operations.MarkUnreadThreadRequest) -> operations.MarkUnreadThreadResponse:
        r"""markUnreadThread
        Mark thread as unread
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.MarkUnreadThreadRequest, base_url, '/v1/message/threads/{id}/unread', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkUnreadThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def search_threads(self, request: shared.SearchParams) -> operations.SearchThreadsResponse:
        r"""searchThreads
        Search for threads of email messages.
        
        Messages with no replies yet are treated as threads with single message.
        
        Lucene syntax supported.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/message/threads:search'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchThreadsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SearchThreads200ApplicationJSON])
                res.search_threads_200_application_json_object = out
        elif http_res.status_code == 403:
            pass

        return res

    def trash_thread(self, request: operations.TrashThreadRequest) -> operations.TrashThreadResponse:
        r"""trashThread
        Move a thread to trash
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.TrashThreadRequest, base_url, '/v1/message/threads/{id}/trash', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TrashThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def untrash_thread(self, request: operations.UntrashThreadRequest) -> operations.UntrashThreadResponse:
        r"""untrashThread
        Restore a trashed thread
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UntrashThreadRequest, base_url, '/v1/message/threads/{id}/untrash', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UntrashThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def update_thread(self) -> operations.UpdateThreadResponse:
        r"""updateThread
        Modify thread metadata
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/message/threads'
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateThreadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateThread201ApplicationJSON])
                res.update_thread_201_application_json_object = out
        elif http_res.status_code == 403:
            pass

        return res

    