"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Any, Optional

class Public:
    r"""Public"""
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
        
    def activate_user(self, request: operations.ActivateUserRequest) -> operations.ActivateUserResponse:
        r"""activateUser
        Activates the user
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/public/activate'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "user_activation_payload", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ActivateUserRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ActivateUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [200, 404]:
            pass

        return res

    def confirm_user(self, request: operations.ConfirmUserRequest) -> operations.ConfirmUserResponse:
        r"""confirmUser
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConfirmUserRequest, base_url, '/v2/portal/user/confirm/{id}', request)
        
        query_params = utils.get_query_params(operations.ConfirmUserRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConfirmUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    def create_user(self, request: operations.CreateUserRequest) -> operations.CreateUserResponse:
        r"""creates a user
        Creates a user in cognito pool and db item
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/public/user'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.CreateUserRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddPortalResp])
                res.add_portal_resp = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def get_count_by_email(self, request: operations.GetCountByEmailRequest) -> operations.GetCountByEmailResponse:
        r"""getCountByEmail
        Check Contact by email
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/contact/email/count'
        
        query_params = utils.get_query_params(operations.GetCountByEmailRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCountByEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCountByEmail200ApplicationJSON])
                res.get_count_by_email_200_application_json_object = out

        return res

    def user_exists(self, request: operations.UserExistsRequest) -> operations.UserExistsResponse:
        r"""userExists
        Checks whether a user exists in the customer portal
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/public/user/exists'
        
        query_params = utils.get_query_params(operations.UserExistsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UserExistsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UserExists200ApplicationJSON])
                res.user_exists_200_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UserExists404ApplicationJSON])
                res.user_exists_404_application_json_object = out

        return res

    