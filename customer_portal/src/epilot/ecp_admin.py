"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Any, Optional

class ECPAdmin:
    r"""ECP Admin"""
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
        
    
    def configure_distribution(self, request: operations.ConfigureDistributionRequest, security: operations.ConfigureDistributionSecurity) -> operations.ConfigureDistributionResponse:
        r"""configureDistribution
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/configure-distribution'
        
        query_params = utils.get_query_params(operations.ConfigureDistributionRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConfigureDistributionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ConfigureDistribution200ApplicationJSON])
                res.configure_distribution_200_application_json_object = out

        return res

    
    def create_sso_user(self, request: operations.CreateSSOUserRequest, security: operations.CreateSSOUserSecurity) -> operations.CreateSSOUserResponse:
        r"""creates a sso user
        Creates a sso user as portal user
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/sso/user'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.CreateSSOUserRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSSOUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateSSOUser201ApplicationJSON])
                res.create_sso_user_201_application_json_object = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def delete_portal(self, request: operations.DeletePortalRequest, security: operations.DeletePortalSecurity) -> operations.DeletePortalResponse:
        r"""deletePortal
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/config'
        
        query_params = utils.get_query_params(operations.DeletePortalRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePortalResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def extra_permission_attributes(self) -> operations.ExtraPermissionAttributesResponse:
        r"""extraPermissionAttributes
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/extra-permission-attributes'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ExtraPermissionAttributesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ExtraPermissionAttributes200ApplicationJSON])
                res.extra_permission_attributes_200_application_json_object = out

        return res

    
    def get_all_portal_configs(self) -> operations.GetAllPortalConfigsResponse:
        r"""getAllPortalConfigs
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/configs'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllPortalConfigsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllPortalConfigs200ApplicationJSON])
                res.get_all_portal_configs_200_application_json_object = out

        return res

    
    def get_ecp_contact(self, request: operations.GetECPContactRequest, security: operations.GetECPContactSecurity) -> operations.GetECPContactResponse:
        r"""getECPContact
        Get the Contact by id
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/ecp/contact'
        
        query_params = utils.get_query_params(operations.GetECPContactRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetECPContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_email_templates(self, request: operations.GetEmailTemplatesRequest, security: operations.GetEmailTemplatesSecurity) -> operations.GetEmailTemplatesResponse:
        r"""getEmailTemplates
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/email-templates'
        
        query_params = utils.get_query_params(operations.GetEmailTemplatesRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEmailTemplatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EmailTemplates])
                res.email_templates = out

        return res

    
    def get_entity_identifiers(self, request: operations.GetEntityIdentifiersRequest, security: operations.GetEntityIdentifiersSecurity) -> operations.GetEntityIdentifiersResponse:
        r"""getEntityIdentifiers
        Get Entity's Identifiers
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetEntityIdentifiersRequest, base_url, '/v2/portal/entity/identifiers/{slug}', request)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEntityIdentifiersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEntityIdentifiers200ApplicationJSON])
                res.get_entity_identifiers_200_application_json_object = out

        return res

    
    def get_org_portal_config(self, request: operations.GetOrgPortalConfigRequest, security: operations.GetOrgPortalConfigSecurity) -> operations.GetOrgPortalConfigResponse:
        r"""getOrgPortalConfig
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/org/portal/config'
        
        query_params = utils.get_query_params(operations.GetOrgPortalConfigRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out

        return res

    
    def get_portal_config(self, request: operations.GetPortalConfigRequest, security: operations.GetPortalConfigSecurity) -> operations.GetPortalConfigResponse:
        r"""getPortalConfig
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/config'
        
        query_params = utils.get_query_params(operations.GetPortalConfigRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out

        return res

    
    def get_public_portal_config(self, request: operations.GetPublicPortalConfigRequest) -> operations.GetPublicPortalConfigResponse:
        r"""getPublicPortalConfig
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/public/portal/config'
        
        query_params = utils.get_query_params(operations.GetPublicPortalConfigRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPublicPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out

        return res

    
    def get_valid_secondary_attributes(self) -> operations.GetValidSecondaryAttributesResponse:
        r"""getValidSecondaryAttributes
        Get Valid Secondary Attributes
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/contact/valid/secondary/attributes'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetValidSecondaryAttributesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetValidSecondaryAttributes200ApplicationJSON])
                res.get_valid_secondary_attributes_200_application_json_object = out

        return res

    
    def replace_ecp_template_variables(self, request: operations.ReplaceECPTemplateVariablesRequest, security: operations.ReplaceECPTemplateVariablesSecurity) -> operations.ReplaceECPTemplateVariablesResponse:
        r"""replaceECPTemplateVariables
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/replace-ecp-template-variables'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.ReplaceECPTemplateVariablesRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReplaceECPTemplateVariablesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ReplaceECPTemplateVariables200ApplicationJSON])
                res.replace_ecp_template_variables_200_application_json_object = out

        return res

    
    def save_portal_files(self, request: shared.SavePortalFile, security: operations.SavePortalFilesSecurity) -> operations.SavePortalFilesResponse:
        r"""Add files to portal
        Add files to portal
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/portal/files'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SavePortalFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def upsert_email_templates(self, request: operations.UpsertEmailTemplatesRequest, security: operations.UpsertEmailTemplatesSecurity) -> operations.UpsertEmailTemplatesResponse:
        r"""upsertEmailTemplates
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/email-templates'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "email_templates", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpsertEmailTemplatesRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertEmailTemplatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpsertEmailTemplates200ApplicationJSON])
                res.upsert_email_templates_200_application_json_object = out

        return res

    
    def upsert_portal(self, request: operations.UpsertPortalRequest, security: operations.UpsertPortalSecurity) -> operations.UpsertPortalResponse:
        r"""upserts a portal
        upserts a portal and db item
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/portal'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "upsert_portal_config", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpsertPortalRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertPortalResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddPortalResp])
                res.add_portal_resp = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    