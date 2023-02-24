import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Any, Optional

class Journeys:
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

    
    def create_journey(self, request: operations.CreateJourneyRequest) -> operations.CreateJourneyResponse:
        r"""createJourney
        Create a Journey
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/journey/configuration"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateJourneyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.journey_response = out

        return res

    
    def get_journey(self, request: operations.GetJourneyRequest) -> operations.GetJourneyResponse:
        r"""getJourney
        Get journey by id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/journey/configuration/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetJourneyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.journey_response = out

        return res

    
    def get_journeys_by_org_id(self, request: operations.GetJourneysByOrgIDRequest) -> operations.GetJourneysByOrgIDResponse:
        r"""getJourneysByOrgId
        Get all journeys by organization id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/journey/organization/{id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetJourneysByOrgIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.get_journeys_response = out

        return res

    
    def patch_update_journey(self, request: operations.PatchUpdateJourneyRequest) -> operations.PatchUpdateJourneyResponse:
        r"""patchUpdateJourney
        Update a Journey (partially / patch). Support for nested properties updates (e.g. \"property[0].name\").
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/journey/configuration"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PatchUpdateJourneyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.journey_response = out

        return res

    
    def remove_journey(self, request: operations.RemoveJourneyRequest) -> operations.RemoveJourneyResponse:
        r"""removeJourney
        Remove journey by id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/journey/configuration/{id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RemoveJourneyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def search_journeys(self, request: operations.SearchJourneysRequest) -> operations.SearchJourneysResponse:
        r"""searchJourneys
        Search Journeys
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/journey/configuration/search"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SearchJourneysResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SearchJourneysResponse])
                res.search_journeys_response = out

        return res

    
    def update_journey(self, request: operations.UpdateJourneyRequest) -> operations.UpdateJourneyResponse:
        r"""updateJourney
        Update a Journey
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/journey/configuration"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateJourneyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.journey_response = out

        return res

    