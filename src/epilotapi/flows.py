import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Optional

class Flows:
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

    
    def create_flow(self, request: operations.CreateFlowRequest) -> operations.CreateFlowResponse:
        r"""createFlow
        Create new automation flow
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/automation/flows"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateFlowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationFlow])
                res.automation_flow = out

        return res

    
    def delete_flow(self, request: operations.DeleteFlowRequest) -> operations.DeleteFlowResponse:
        r"""deleteFlow
        Update automation flow by id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/flows/{flow_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteFlowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationFlow])
                res.automation_flow = out

        return res

    
    def get_flow(self, request: operations.GetFlowRequest) -> operations.GetFlowResponse:
        r"""getFlow
        List available automation flows
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/flows/{flow_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetFlowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationFlow])
                res.automation_flow = out

        return res

    
    def put_flow(self, request: operations.PutFlowRequest) -> operations.PutFlowResponse:
        r"""putFlow
        Update automation flow by id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/flows/{flow_id}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutFlowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationFlow])
                res.automation_flow = out

        return res

    
    def search_flows(self, request: operations.SearchFlowsRequest) -> operations.SearchFlowsResponse:
        r"""searchFlows
        Search available automation flows
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/automation/flows"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.SearchFlowsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SearchAutomationsResp])
                res.search_automations_resp = out

        return res

    