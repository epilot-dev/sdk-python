"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Optional

class Webhooks:
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
        
    def create_config(self, request: shared.WebhookConfig) -> operations.CreateConfigResponse:
        r"""createConfig
        Create Webhook Client Config
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/configs'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WebhookConfig])
                res.webhook_config = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def delete_config(self, request: operations.DeleteConfigRequest) -> operations.DeleteConfigResponse:
        r"""deleteConfig
        Delete Webhook Client Config
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteConfigRequest, base_url, '/v1/webhooks/configs/{configId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [204, 404]:
            pass
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def get_config(self, request: operations.GetConfigRequest) -> operations.GetConfigResponse:
        r"""getConfig
        Get webhook config by id
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetConfigRequest, base_url, '/v1/webhooks/configs/{configId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WebhookConfig])
                res.webhook_config = out
        elif http_res.status_code in [404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def get_configs(self, request: operations.GetConfigsRequest) -> operations.GetConfigsResponse:
        r"""getConfigs
        Search Webhook Client Configs
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/configs'
        
        query_params = utils.get_query_params(operations.GetConfigsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConfigsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.WebhookConfig]])
                res.webhook_configs = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def get_configured_events(self) -> operations.GetConfiguredEventsResponse:
        r"""getConfiguredEvents
        Retrieve events that can trigger webhooks
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/configured-events'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConfiguredEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.EventConfigEntry]])
                res.event_config_resp = out

        return res

    def get_failures(self, request: operations.GetFailuresRequest) -> operations.GetFailuresResponse:
        r"""getFailures
        Get saved failures from the webhooks DB, in a paginated way
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/failures'
        
        query_params = utils.get_query_params(operations.GetFailuresRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFailuresResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailuresResp])
                res.failures_resp = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def resend_failure(self, request: shared.FailureEntry) -> operations.ResendFailureResponse:
        r"""resendFailure
        Resend payload for one failure
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/failures/resend'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ResendFailureResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    def update_config(self, request: operations.UpdateConfigRequest) -> operations.UpdateConfigResponse:
        r"""updateConfig
        Update Webhook Client Config
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateConfigRequest, base_url, '/v1/webhooks/configs/{configId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "webhook_config", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WebhookConfig])
                res.webhook_config = out
        elif http_res.status_code in [400, 401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResp])
                res.error_resp = out

        return res

    