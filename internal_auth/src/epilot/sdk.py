"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import operations
from typing import Any, Optional

class Epilot:
    r"""Internal Auth API: Auth API to provide JWT tokens for internal API access that work with the epilot custom authorizer.

    Converts AWS credentials into a JWT token with caller's ARN `callerIdentity` and list of `policies` granting access to API Gateway as claims.
    """

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = client
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx)
       
        
    
    
    
    def get_jwks(self) -> operations.GetJwksResponse:
        r"""getJwks
        Get jwks public key set to verify tokens generated by this API
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/.well-known/jwks.json'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/.well-known/openid-configuration'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/auth'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/auth'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTokenV2Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTokenV2200ApplicationJSON])
                res.get_token_v2_200_application_json_object = out

        return res

    