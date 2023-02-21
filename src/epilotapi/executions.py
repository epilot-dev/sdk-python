import requests
from . import utils
from epilotapi.models import operations, shared
from typing import Optional

class Executions:
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

    
    def cancel_execution(self, request: operations.CancelExecutionRequest) -> operations.CancelExecutionResponse:
        r"""cancelExecution
        Cancel automation execution
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/executions/{execution_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.CancelExecutionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    
    def get_execution(self, request: operations.GetExecutionRequest) -> operations.GetExecutionResponse:
        r"""getExecution
        Get automation execution
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/executions/{execution_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetExecutionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    
    def get_executions(self, request: operations.GetExecutionsRequest) -> operations.GetExecutionsResponse:
        r"""getExecutions
        List automation executions
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/automation/executions"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetExecutionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.GetExecutionsResp])
                res.get_executions_resp = out

        return res

    
    def retrigger_action(self, request: operations.RetriggerActionRequest) -> operations.RetriggerActionResponse:
        r"""retriggerAction
        Retry a specific automation execution action which failed / is stuck.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/automation/executions/{execution_id}/{action_id}/retrigger", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RetriggerActionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def start_execution(self, request: operations.StartExecutionRequest) -> operations.StartExecutionResponse:
        r"""startExecution
        Start new automation execution
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/automation/executions"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.StartExecutionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    