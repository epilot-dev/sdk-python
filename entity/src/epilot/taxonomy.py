"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Taxonomy:
    r"""Entity classification with Taxonomies"""
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
        
    
    def get_taxonomy(self, request: operations.GetTaxonomyRequest) -> operations.GetTaxonomyResponse:
        r"""getTaxonomy
        Get taxonomy by slug
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTaxonomyRequest, base_url, '/v1/entity/taxonomies/{taxonomySlug}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTaxonomyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Taxonomy])
                res.taxonomy = out

        return res

    
    def list_taxonomies(self) -> operations.ListTaxonomiesResponse:
        r"""listTaxonomies
        List taxonomies in an organisation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity/listTaxonomies'
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListTaxonomiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListTaxonomies200ApplicationJSON])
                res.list_taxonomies_200_application_json_object = out

        return res

    
    def taxonomies_classifications_search(self, request: operations.TaxonomiesClassificationsSearchRequest) -> operations.TaxonomiesClassificationsSearchResponse:
        r"""taxonomiesClassificationsSearch
        List taxonomy classifications in an organisation based on taxonomy slug
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/entity/taxonomies/classifications:search'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.TaxonomiesClassificationsSearchRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TaxonomiesClassificationsSearchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.TaxonomiesClassificationsSearch200ApplicationJSON])
                res.taxonomies_classifications_search_200_application_json_object = out

        return res

    
    def taxonomy_autocomplete(self, request: operations.TaxonomyAutocompleteRequest) -> operations.TaxonomyAutocompleteResponse:
        r"""taxonomyAutocomplete
        Taxonomies autocomplete
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.TaxonomyAutocompleteRequest, base_url, '/v1/entity/taxonomies/{taxonomySlug}:autocomplete', request)
        headers = {}
        query_params = utils.get_query_params(operations.TaxonomyAutocompleteRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TaxonomyAutocompleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.TaxonomyAutocomplete200ApplicationJSON])
                res.taxonomy_autocomplete_200_application_json_object = out

        return res

    
    def update_classifications_for_taxonomy(self, request: operations.UpdateClassificationsForTaxonomyRequest) -> operations.UpdateClassificationsForTaxonomyResponse:
        r"""updateClassificationsForTaxonomy
        Update taxonomies in an organisation based in taxonomy slug
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateClassificationsForTaxonomyRequest, base_url, '/v1/entity/taxonomies/{taxonomySlug}/classifications', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "classifications_update", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateClassificationsForTaxonomyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateClassificationsForTaxonomy200ApplicationJSON])
                res.update_classifications_for_taxonomy_200_application_json_object = out

        return res

    