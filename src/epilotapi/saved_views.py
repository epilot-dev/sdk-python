import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Optional

class SavedViews:
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

    
    def create_saved_view(self, request: operations.CreateSavedViewRequest) -> operations.CreateSavedViewResponse:
        r"""createSavedView
        Creates a new saved view
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/view"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateSavedViewResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SavedViewItem])
                res.saved_view_item = out

        return res

    
    def delete_saved_view(self, request: operations.DeleteSavedViewRequest) -> operations.DeleteSavedViewResponse:
        r"""deleteSavedView
        Deletes a saved view
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/view/{id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteSavedViewResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_saved_view(self, request: operations.GetSavedViewRequest) -> operations.GetSavedViewResponse:
        r"""getSavedView
        Gets Saved View configuration by id.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/view/{id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSavedViewResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSavedView200ApplicationJSON])
                res.get_saved_view_200_application_json_object = out

        return res

    
    def list_saved_views(self) -> operations.ListSavedViewsResponse:
        r"""listSavedViews
        Get the Saved Views based on the schema
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/entity/views"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSavedViewsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSavedViews200ApplicationJSON])
                res.list_saved_views_200_application_json_object = out

        return res

    
    def update_saved_view(self, request: operations.UpdateSavedViewRequest) -> operations.UpdateSavedViewResponse:
        r"""updateSavedView
        Updates a saved view
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/entity/view/{id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateSavedViewResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SavedViewItem])
                res.saved_view_item = out

        return res

    