"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Any, Optional

class Roles:
    r"""Manage roles and grants"""
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
        
    def delete_role(self, request: operations.DeleteRoleRequest) -> operations.DeleteRoleResponse:
        r"""deleteRole
        Delete role by id
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteRoleRequest, base_url, '/v1/permissions/roles/{roleId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteRoleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.role = out

        return res

    def get_role(self, request: operations.GetRoleRequest) -> operations.GetRoleResponse:
        r"""getRole
        Get role by id
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetRoleRequest, base_url, '/v1/permissions/roles/{roleId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.role = out

        return res

    def list_all_roles(self) -> operations.ListAllRolesResponse:
        r"""listAllRoles
        Returns list of all roles in organization
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/permissions/roles'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllRolesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListAllRoles200ApplicationJSON])
                res.list_all_roles_200_application_json_object = out

        return res

    def list_current_roles(self) -> operations.ListCurrentRolesResponse:
        r"""listCurrentRoles
        Returns roles and grants assigned to current user
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/permissions/me'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCurrentRolesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCurrentRoles200ApplicationJSON])
                res.list_current_roles_200_application_json_object = out

        return res

    def put_role(self, request: operations.PutRoleRequest) -> operations.PutRoleResponse:
        r"""putRole
        Create or update role
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutRoleRequest, base_url, '/v1/permissions/roles/{roleId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutRoleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.role = out

        return res

    def refresh_permissions(self) -> operations.RefreshPermissionsResponse:
        r"""refreshPermissions
        Makes sure the user has a role in the organization
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/permissions/refresh'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RefreshPermissionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    def search_roles(self, request: shared.RoleSearchInput) -> operations.SearchRolesResponse:
        r"""searchRoles
        Search Roles
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/permissions/roles:search'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchRolesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SearchRoles200ApplicationJSON])
                res.search_roles_200_application_json_object = out

        return res

    