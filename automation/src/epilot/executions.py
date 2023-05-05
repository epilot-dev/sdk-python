"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Executions:
    r"""Automation executions"""
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
        
    
    def cancel_execution(self, request: operations.CancelExecutionRequest) -> operations.CancelExecutionResponse:
        r"""cancelExecution
        Cancel automation execution
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CancelExecutionRequest, base_url, '/v1/automation/executions/{execution_id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CancelExecutionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    
    def get_execution(self, request: operations.GetExecutionRequest) -> operations.GetExecutionResponse:
        r"""getExecution
        Get automation execution
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetExecutionRequest, base_url, '/v1/automation/executions/{execution_id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetExecutionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    
    def get_executions(self, request: operations.GetExecutionsRequest) -> operations.GetExecutionsResponse:
        r"""getExecutions
        List automation executions
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/automation/executions'
        
        query_params = utils.get_query_params(operations.GetExecutionsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetExecutionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetExecutionsResp])
                res.get_executions_resp = out

        return res

    
    def retrigger_action(self, request: operations.RetriggerActionRequest) -> operations.RetriggerActionResponse:
        r"""retriggerAction
        Retry a specific automation execution action which failed / is stuck.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetriggerActionRequest, base_url, '/v1/automation/executions/{execution_id}/{action_id}/retrigger', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "retry_req", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetriggerActionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def start_execution(self, request: shared.StartExecutionRequestInput) -> operations.StartExecutionResponse:
        r"""startExecution
        Start new automation execution
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/automation/executions'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.StartExecutionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationExecution])
                res.automation_execution = out

        return res

    