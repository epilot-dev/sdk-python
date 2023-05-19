"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Any, Optional

class Ecp:
    r"""ECP"""
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
        
    
    def add_end_customer_relation_to_entity(self, request: operations.AddEndCustomerRelationToEntityRequest, security: operations.AddEndCustomerRelationToEntitySecurity) -> operations.AddEndCustomerRelationToEntityResponse:
        r"""addEndCustomerRelationToEntity
        Add EndCustomer Relation To an Entity
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddEndCustomerRelationToEntityRequest, base_url, '/v2/portal/entity/add-end-customer/{slug}/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PUT', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddEndCustomerRelationToEntityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.AddEndCustomerRelationToEntity200ApplicationJSON])
                res.add_end_customer_relation_to_entity_200_application_json_object = out

        return res

    
    def delete_entity_file(self, request: shared.DeleteEntityFile, security: operations.DeleteEntityFileSecurity) -> operations.DeleteEntityFileResponse:
        r"""Delete files from an entity
        Delete files from an entity
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/entity/file'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteEntityFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteEntityFile200ApplicationJSON])
                res.delete_entity_file_200_application_json_object = out

        return res

    
    def delete_portal_user(self, security: operations.DeletePortalUserSecurity) -> operations.DeletePortalUserResponse:
        r"""deletePortalUser
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/user'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePortalUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.delete_portal_user_200_application_json_string = http_res.content

        return res

    
    def get_all_contracts(self, security: operations.GetAllContractsSecurity) -> operations.GetAllContractsResponse:
        r"""getAllContracts
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/contract'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllContractsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllContracts200ApplicationJSON])
                res.get_all_contracts_200_application_json_object = out

        return res

    
    def get_all_opportunities(self, security: operations.GetAllOpportunitiesSecurity) -> operations.GetAllOpportunitiesResponse:
        r"""getAllOpportunities
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/opportunity'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllOpportunitiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllOpportunities200ApplicationJSON])
                res.get_all_opportunities_200_application_json_object = out

        return res

    
    def get_all_orders(self, security: operations.GetAllOrdersSecurity) -> operations.GetAllOrdersResponse:
        r"""getAllOrders
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/order'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllOrdersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllOrders200ApplicationJSON])
                res.get_all_orders_200_application_json_object = out

        return res

    
    def get_contact(self, security: operations.GetContactSecurity) -> operations.GetContactResponse:
        r"""getContact
        Get the Contact by id
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/contact'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContact200ApplicationJSON])
                res.get_contact_200_application_json_object = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    
    def get_contract(self, request: operations.GetContractRequest, security: operations.GetContractSecurity) -> operations.GetContractResponse:
        r"""get contract based on id
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetContractRequest, base_url, '/v2/portal/contract/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract200ApplicationJSON])
                res.get_contract_200_application_json_object = out

        return res

    
    def get_entities_by_identifiers(self, request: operations.GetEntitiesByIdentifiersRequest, security: operations.GetEntitiesByIdentifiersSecurity) -> operations.GetEntitiesByIdentifiersResponse:
        r"""getEntitiesByIdentifiers
        Get Entities By Identifiers
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetEntitiesByIdentifiersRequest, base_url, '/v2/portal/entity/by-identifiers/{slug}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEntitiesByIdentifiersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetEntitiesByIdentifiers200ApplicationJSON])
                res.get_entities_by_identifiers_200_application_json_object = out

        return res

    
    def get_opportunity(self, request: operations.GetOpportunityRequest, security: operations.GetOpportunitySecurity) -> operations.GetOpportunityResponse:
        r"""getOpportunity
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOpportunityRequest, base_url, '/v2/portal/opportunities/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOpportunityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOpportunity200ApplicationJSON])
                res.get_opportunity_200_application_json_object = out

        return res

    
    def get_order(self, request: operations.GetOrderRequest, security: operations.GetOrderSecurity) -> operations.GetOrderResponse:
        r"""getOrder
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrderRequest, base_url, '/v2/portal/order/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrderResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOrder200ApplicationJSON])
                res.get_order_200_application_json_object = out

        return res

    
    def get_organization_settings(self, security: operations.GetOrganizationSettingsSecurity) -> operations.GetOrganizationSettingsResponse:
        r"""getOrganizationSettings
        get organization settings
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/org/settings'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrganizationSettingsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSettings])
                res.organization_settings = out

        return res

    
    def get_portal_config(self, request: operations.GetPortalConfigRequest, security: operations.GetPortalConfigSecurity) -> operations.GetPortalConfigResponse:
        r"""getPortalConfig
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/config'
        headers = {}
        query_params = utils.get_query_params(operations.GetPortalConfigRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPortalConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out

        return res

    
    def get_portal_config_by_domain(self, request: operations.GetPortalConfigByDomainRequest) -> operations.GetPortalConfigByDomainResponse:
        r"""getPortalConfigByDomain
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/public/config'
        headers = {}
        query_params = utils.get_query_params(operations.GetPortalConfigByDomainRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPortalConfigByDomainResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PortalConfig])
                res.portal_config = out

        return res

    
    def get_portal_user(self, security: operations.GetPortalUserSecurity) -> operations.GetPortalUserResponse:
        r"""getPortalUser
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/user'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPortalUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def get_schemas(self, security: operations.GetSchemasSecurity) -> operations.GetSchemasResponse:
        r"""getSchemas
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/schemas'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSchemasResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSchemas200ApplicationJSON])
                res.get_schemas_200_application_json_object = out

        return res

    
    def save_entity_file(self, request: shared.SaveEntityFile, security: operations.SaveEntityFileSecurity) -> operations.SaveEntityFileResponse:
        r"""Add files to an entity
        Add files to an entity
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/entity/file'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SaveEntityFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SaveEntityFile200ApplicationJSON])
                res.save_entity_file_200_application_json_object = out

        return res

    
    def test_auth(self) -> operations.TestAuthResponse:
        r"""testAuth
        TODO
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/auth'
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TestAuthResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def update_contact(self, request: dict[str, Any], security: operations.UpdateContactSecurity) -> operations.UpdateContactResponse:
        r"""updateContact
        Update the contact details
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/contact'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def update_contract(self, request: operations.UpdateContractRequest, security: operations.UpdateContractSecurity) -> operations.UpdateContractResponse:
        r"""Update contract based on id
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateContractRequest, base_url, '/v2/portal/contract/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract200ApplicationJSON])
                res.update_contract_200_application_json_object = out

        return res

    
    def update_opportunity(self, request: operations.UpdateOpportunityRequest, security: operations.UpdateOpportunitySecurity) -> operations.UpdateOpportunityResponse:
        r"""Update an opportunity based on id
        TODO
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateOpportunityRequest, base_url, '/v2/portal/opportunities/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOpportunityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateOpportunity200ApplicationJSON])
                res.update_opportunity_200_application_json_object = out

        return res

    
    def update_order(self, request: operations.UpdateOrderRequest, security: operations.UpdateOrderSecurity) -> operations.UpdateOrderResponse:
        r"""updateOrder
        Update the order details
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateOrderRequest, base_url, '/v2/portal/order/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOrderResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    
    def update_portal_user(self, request: dict[str, Any], security: operations.UpdatePortalUserSecurity) -> operations.UpdatePortalUserResponse:
        r"""updatePortalUser
        Update the portal user details
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v2/portal/user'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdatePortalUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.entity_item = out

        return res

    