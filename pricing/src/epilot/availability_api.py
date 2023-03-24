"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from epilot.models import operations, shared
from typing import Any, Optional

class AvailabilityAPI:
    r"""Provides endpoints for querying products availability by a set of predefined dimensions.
    
    """
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
        
    def dollar_availability_check(self, request: operations.DollarAvailabilityCheckRequest) -> operations.DollarAvailabilityCheckResponse:
        r"""availabilityCheck
        The availability check endpoint
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/public/availability:check'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "availability_check_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DollarAvailabilityCheckResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AvailabilityResult])
                res.availability_result = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.error = out

        return res

    