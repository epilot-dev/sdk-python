"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations
from typing import Optional

class Public:
    r"""Well known endpoints to verify tokens generated by this API"""
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
        
    
    def get_access_token_jwks(self) -> operations.GetAccessTokenJwksResponse:
        r"""getAccessTokenJwks
        Get jwks public key set to verify access tokens generated by this API
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/access-tokens/.well-known/jwks.json'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccessTokenJwksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccessTokenJwks200ApplicationJSON])
                res.get_access_token_jwks_200_application_json_object = out

        return res

    
    def get_access_token_oidc(self) -> operations.GetAccessTokenOIDCResponse:
        r"""getAccessTokenOIDC
        OpenID Connect configuration for Access Token API as identity provider
        
        Note: This API is not a fully compliant OAuth2.0 / OIDC identity provider, but this endpoint is useful to
        automate the process of verifying JWT tokens.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/access-tokens/.well-known/openid-configuration'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccessTokenOIDCResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAccessTokenOIDC200ApplicationJSON])
                res.get_access_token_oidc_200_application_json_object = out

        return res

    
    def get_public_token_jwks(self) -> operations.GetPublicTokenJwksResponse:
        r"""getPublicTokenJwks
        Get jwks public key set to verify public tokens generated by this API
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/access-tokens/public/.well-known/jwks.json'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPublicTokenJwksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPublicTokenJwks200ApplicationJSON])
                res.get_public_token_jwks_200_application_json_object = out

        return res

    
    def get_public_token_oidc(self) -> operations.GetPublicTokenOIDCResponse:
        r"""getPublicTokenOIDC
        OpenID Connect configuration for Access Token API a a public identity provider
        
        Note: This API is not a fully compliant OAuth2.0 / OIDC identity provider, but this endpoint is useful to
        automate the process of verifying JWT tokens.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/access-tokens/public/.well-known/openid-configuration'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPublicTokenOIDCResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPublicTokenOIDC200ApplicationJSON])
                res.get_public_token_oidc_200_application_json_object = out

        return res

    