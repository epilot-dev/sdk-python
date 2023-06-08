"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import operations, shared
from typing import Any, Optional

class AccessTokens:
    r"""Create Access Tokens for epilot APIs"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_access_token(self, request: Any) -> operations.CreateAccessTokenResponse:
        r"""createAccessToken
        **Access Token type: `API`** (default if not specified):
        
        Generates a new Access Token to use for calling epilot APIs.
        
        Takes optionally a list of Roles assigned to the Access Token. Defaults to current user's assignments
        
        See [Permissions API docs](https://docs.epilot.io/api/permissions)
        
        **Access Token type: `JOURNEY`**:
        
        Generates a Public Access Token related to a journey.
        The journey id should be specfied.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/access-tokens'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAccessTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateAccessToken201ApplicationJSON])
                res.create_access_token_201_application_json_object = out

        return res

    
    def list_access_tokens(self, request: operations.ListAccessTokensRequest) -> operations.ListAccessTokensResponse:
        r"""listAccessTokens
        Lists all Access Tokens for current user (by default excludes system generated tokens)
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/access-tokens'
        headers = {}
        query_params = utils.get_query_params(operations.ListAccessTokensRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAccessTokensResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.AccessTokenItem]])
                res.access_token_items = out

        return res

    
    def revoke_access_token(self, request: operations.RevokeAccessTokenRequest) -> operations.RevokeAccessTokenResponse:
        r"""revokeAccessToken
        Revokes an Access Token so it can't be used anymore.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RevokeAccessTokenRequest, base_url, '/v1/access-tokens/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeAccessTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccessTokenItem])
                res.access_token_item = out

        return res

    