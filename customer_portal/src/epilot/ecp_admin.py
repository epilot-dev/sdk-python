"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import operations, shared
from typing import Optional

class ECPAdmin:
    r"""APIs defined for a ECP Admin"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def configure_distribution(self, request: operations.ConfigureDistributionRequest, security: operations.ConfigureDistributionSecurity) -> operations.ConfigureDistributionResponse:
        r"""configureDistribution
        Configure the distribution for the portal's custom domain
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/configure-distribution'
        headers = {}
        query_params = utils.get_query_params(operations.ConfigureDistributionRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConfigureDistributionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ConfigureDistribution200ApplicationJSON])
                res.configure_distribution_200_application_json_object = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def create_sso_user(self, request: operations.CreateSSOUserRequest, security: operations.CreateSSOUserSecurity) -> operations.CreateSSOUserResponse:
        r"""createSSOUser
        Creates a portal user as an SSO user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/sso/user'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_sso_user_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.CreateSSOUserRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
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
        Deletes the portal.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/config'
        headers = {}
        query_params = utils.get_query_params(operations.DeletePortalRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePortalResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def extra_permission_attributes(self, security: operations.ExtraPermissionAttributesSecurity) -> operations.ExtraPermissionAttributesResponse:
        r"""extraPermissionAttributes
        Retrieves the extra permission attributes.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/extra-permission-attributes'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ExtraPermissionAttributesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ExtraPermissionAttributes200ApplicationJSON])
                res.extra_permission_attributes_200_application_json_object = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_all_portal_configs(self, security: operations.GetAllPortalConfigsSecurity) -> operations.GetAllPortalConfigsResponse:
        r"""getAllPortalConfigs
        Retrieves all portal configurations.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/configs'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllPortalConfigsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllPortalConfigs200ApplicationJSON])
                res.get_all_portal_configs_200_application_json_object = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_ecp_contact(self, request: operations.GetECPContactRequest, security: operations.GetECPContactSecurity) -> operations.GetECPContactResponse:
        r"""getECPContact
        Get the Contact by id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/ecp/contact'
        headers = {}
        query_params = utils.get_query_params(operations.GetECPContactRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetECPContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetECPContact200ApplicationJSON])
                res.get_ecp_contact_200_application_json_object = out
        elif http_res.status_code in [401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_email_templates(self, request: operations.GetEmailTemplatesRequest, security: operations.GetEmailTemplatesSecurity) -> operations.GetEmailTemplatesResponse:
        r"""getEmailTemplates
        Retrieves the email templates of a portal
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/email-templates'
        headers = {}
        query_params = utils.get_query_params(operations.GetEmailTemplatesRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEmailTemplatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EmailTemplates])
                res.email_templates = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_entity_identifiers(self, request: operations.GetEntityIdentifiersRequest, security: operations.GetEntityIdentifiersSecurity) -> operations.GetEntityIdentifiersResponse:
        r"""getEntityIdentifiers
        Retrieve a list of entity identifiers used for entity search by portal users.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetEntityIdentifiersRequest, base_url, '/v2/portal/entity/identifiers/{slug}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEntityIdentifiersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEntityIdentifiers200ApplicationJSON])
                res.get_entity_identifiers_200_application_json_object = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_org_portal_config(self, request: operations.GetOrgPortalConfigRequest, security: operations.GetOrgPortalConfigSecurity) -> operations.GetOrgPortalConfigResponse:
        r"""getOrgPortalConfig
        Retrieves the portal configuration for the organization.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/org/portal/config'
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgPortalConfigRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_portal_config(self, request: operations.GetPortalConfigRequest, security: operations.GetPortalConfigSecurity) -> operations.GetPortalConfigResponse:
        r"""getPortalConfig
        Retrieves the portal configuration.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/config'
        headers = {}
        query_params = utils.get_query_params(operations.GetPortalConfigRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_valid_secondary_attributes(self, security: operations.GetValidSecondaryAttributesSecurity) -> operations.GetValidSecondaryAttributesResponse:
        r"""getValidSecondaryAttributes
        Get valid secondary attributes that are used while mapping a contact on registration
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/contact/valid/secondary/attributes'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetValidSecondaryAttributesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetValidSecondaryAttributes200ApplicationJSON])
                res.get_valid_secondary_attributes_200_application_json_object = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def replace_ecp_template_variables(self, request: operations.ReplaceECPTemplateVariablesRequest, security: operations.ReplaceECPTemplateVariablesSecurity) -> operations.ReplaceECPTemplateVariablesResponse:
        r"""replaceECPTemplateVariables
        Replaces the template variables of a portal
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/replace-ecp-template-variables'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.ReplaceECPTemplateVariablesRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReplaceECPTemplateVariablesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ReplaceECPTemplateVariables200ApplicationJSON])
                res.replace_ecp_template_variables_200_application_json_object = out
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def save_portal_files(self, request: shared.SavePortalFile, security: operations.SavePortalFilesSecurity) -> operations.SavePortalFilesResponse:
        r"""savePortalFiles
        Add files to portal
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/portal/files'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SavePortalFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SavePortalFiles201ApplicationJSON])
                res.save_portal_files_201_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def upsert_email_templates(self, request: operations.UpsertEmailTemplatesRequest, security: operations.UpsertEmailTemplatesSecurity) -> operations.UpsertEmailTemplatesResponse:
        r"""upsertEmailTemplates
        Upserts the email templates of a portal
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/email-templates'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "email_templates", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpsertEmailTemplatesRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertEmailTemplatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpsertEmailTemplates200ApplicationJSON])
                res.upsert_email_templates_200_application_json_object = out
        elif http_res.status_code in [401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def upsert_portal(self, request: operations.UpsertPortalRequest, security: operations.UpsertPortalSecurity) -> operations.UpsertPortalResponse:
        r"""upsertPortal
        Upserts the settings for a portal of an organization.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/portal/portal'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "upsert_portal_config", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpsertPortalRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertPortalResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out
        elif http_res.status_code in [400, 401, 403, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    