"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass

from .utils.retries import RetryConfig


SERVERS = [
    'https://pricing-api.sls.epilot.io',
    'https://pricing-api.sls.epilot.io',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.43.1'
    gen_version: str = '2.143.2'
    user_agent: str = 'speakeasy-sdk/python 1.43.1 2.143.2 1.0.0 epilot-pricing'
    retry_config: RetryConfig = None

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
