"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations
from typing import Any, Optional

class Messages:
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
        
    def delete_message(self, request: operations.DeleteMessageRequest) -> operations.DeleteMessageResponse:
        r"""deleteMessage
        Immediately and permanently delete a message. This operation cannot be undone.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteMessageRequest, base_url, '/v1/message/messages/{id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 403]:
            pass

        return res

    def get_message(self, request: operations.GetMessageRequest) -> operations.GetMessageResponse:
        r"""getMessage
        Get an email message by id
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetMessageRequest, base_url, '/v1/message/messages/{id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetMessage201ApplicationJSON])
                res.get_message_201_application_json_object = out
        elif http_res.status_code == 403:
            pass

        return res

    def mark_read_message(self, request: operations.MarkReadMessageRequest) -> operations.MarkReadMessageResponse:
        r"""markReadMessage
        Mark message as read
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.MarkReadMessageRequest, base_url, '/v1/message/messages/{id}/read', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkReadMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 403]:
            pass

        return res

    def mark_unread_message(self, request: operations.MarkUnreadMessageRequest) -> operations.MarkUnreadMessageResponse:
        r"""markUnreadMessage
        Mark message as unread
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.MarkUnreadMessageRequest, base_url, '/v1/message/messages/{id}/unread', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MarkUnreadMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 403]:
            pass

        return res

    def send_message(self, request: Any) -> operations.SendMessageResponse:
        r"""sendMessage
        Send an email message
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/message/messages'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SendMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SendMessage201ApplicationJSON])
                res.send_message_201_application_json_object = out
        elif http_res.status_code == 403:
            pass

        return res

    def trash_message(self, request: operations.TrashMessageRequest) -> operations.TrashMessageResponse:
        r"""trashMessage
        Move a message to the trash
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.TrashMessageRequest, base_url, '/v1/message/messages/{id}/trash', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TrashMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 403]:
            pass

        return res

    def untrash_message(self, request: operations.UntrashMessageRequest) -> operations.UntrashMessageResponse:
        r"""untrashMessage
        Restore a trashed message
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UntrashMessageRequest, base_url, '/v1/message/messages/{id}/untrash', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UntrashMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 403]:
            pass

        return res

    def update_message(self) -> operations.UpdateMessageResponse:
        r"""updateMessage
        Update message metadata
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/message/messages'
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateMessageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateMessage201ApplicationJSON])
                res.update_message_201_application_json_object = out
        elif http_res.status_code == 403:
            pass

        return res

    