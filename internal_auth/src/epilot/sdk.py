"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations
from typing import Any, Optional

SERVERS = [
    "https://internal-auth.sls.epilot.io/v1/internal-auth",
]
"""Contains the list of servers available to the SDK"""

class Epilot:
    r"""Auth API to provide JWT tokens for internal API access that work with the epilot custom authorizer.
    
    Converts AWS credentials into a JWT token with caller's ARN `callerIdentity` and list of `policies` granting access to API Gateway as claims.
    
    """

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.2"
    _gen_version: str = "2.16.5"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        
    
    
    def get_jwks(self) -> operations.GetJwksResponse:
        r"""getJwks
        Get jwks public key set to verify tokens generated by this API
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/.well-known/jwks.json'
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJwksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetJwks200ApplicationJSON])
                res.get_jwks_200_application_json_object = out

        return res

    def get_open_id_configuration(self) -> operations.GetOpenIDConfigurationResponse:
        r"""getOpenIDConfiguration
        OpenID Connect configuration for internal auth as identity provider
        
        Note: This API is not a fully compliant OAuth2.0 / OIDC identity provider, but this endpoint is useful to
        automate the process of verifying JWT tokens.
        
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/.well-known/openid-configuration'
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOpenIDConfigurationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOpenIDConfiguration200ApplicationJSON])
                res.get_open_id_configuration_200_application_json_object = out

        return res

    def get_token(self, security: operations.GetTokenSecurity) -> operations.GetTokenResponse:
        r"""getToken
        Generates token for internal API access
        
        Example JWT payload:
        
        ```json
        {
          \"callerIdentity\": \"arn:aws:sts::912468240823:assumed-role/ep_prod_access_admin/awsmfa_20210225T193753\",
          \"policies\": [
            {
              \"Version\": \"2012-10-17\",
              \"Statement\": [
                {
                  \"Effect\": \"Allow\",
                  \"Action\": \"*\",
                  \"Resource\": \"*\"
                }
              ]
            }
          ],
          \"iss\": \"https://internal-auth.sls.epilot.io/v1/internal-auth\",
          \"iat\": 1614278397,
          \"exp\": 1614281997
        }
        ```
        
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetToken200ApplicationJSON])
                res.get_token_200_application_json_object = out

        return res

    def get_token_v2(self, request: dict[str, Any], security: operations.GetTokenV2Security) -> operations.GetTokenV2Response:
        r"""getTokenV2
        Generates token for internal API access with internal roles
        
        Example JWT payload:
        
        ```json
        {
          \"callerIdentity\": \"arn:aws:sts::912468240823:assumed-role/ep_prod_access_admin/awsmfa_20210225T193753\",
          \"policies\": [
            {
              \"Version\": \"2012-10-17\",
              \"Statement\": [
                {
                  \"Effect\": \"Allow\",
                  \"Action\": \"*\",
                  \"Resource\": \"*\"
                }
              ]
            }
          ],
          \"assume_roles\": [\"org_id:note_role\", \"org_id:file_role\"],
          \"org_id\": \"org_id\",
          \"iss\": \"https://internal-auth.sls.epilot.io/v1/internal-auth\",
          \"iat\": 1614278397,
          \"exp\": 1614281997
        }
        ```
        
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTokenV2Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTokenV2200ApplicationJSON])
                res.get_token_v2_200_application_json_object = out

        return res

    