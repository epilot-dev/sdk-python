import requests
from typing import Optional
from epilotapi.models import shared, operations
from . import utils

class Taxonomy:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
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
        
        url = utils.generate_url(base_url, "/v1/entity/taxonomies/{taxonomySlug}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTaxonomyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Taxonomy])
                res.taxonomy = out

        return res

    
    def list_taxonomies(self) -> operations.ListTaxonomiesResponse:
        r"""listTaxonomies
        List taxonomies in an organisation
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/listTaxonomies"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListTaxonomiesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListTaxonomies200ApplicationJSON])
                res.list_taxonomies_200_application_json_object = out

        return res

    
    def taxonomies_classifications_search(self, request: operations.TaxonomiesClassificationsSearchRequest) -> operations.TaxonomiesClassificationsSearchResponse:
        r"""taxonomiesClassificationsSearch
        List taxonomy classifications in an organisation based on taxonomy slug
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/taxonomies/classifications:search"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("POST", url, params=query_params, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.TaxonomiesClassificationsSearchResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.TaxonomiesClassificationsSearch200ApplicationJSON])
                res.taxonomies_classifications_search_200_application_json_object = out

        return res

    
    def taxonomy_autocomplete(self, request: operations.TaxonomyAutocompleteRequest) -> operations.TaxonomyAutocompleteResponse:
        r"""taxonomyAutocomplete
        Taxonomies autocomplete
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/taxonomies/{taxonomySlug}:autocomplete", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.TaxonomyAutocompleteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.TaxonomyAutocomplete200ApplicationJSON])
                res.taxonomy_autocomplete_200_application_json_object = out

        return res

    
    def update_classifications_for_taxonomy(self, request: operations.UpdateClassificationsForTaxonomyRequest) -> operations.UpdateClassificationsForTaxonomyResponse:
        r"""updateClassificationsForTaxonomy
        Update taxonomies in an organisation based in taxonomy slug
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/taxonomies/{taxonomySlug}/classifications", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateClassificationsForTaxonomyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateClassificationsForTaxonomy200ApplicationJSON])
                res.update_classifications_for_taxonomy_200_application_json_object = out

        return res

    