"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from epilot.models import components
from typing import Callable, Dict, Tuple, Union


SERVERS = [
    'https://entity.sls.epilot.io',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.3.0'
    gen_version: str = '2.283.1'
    user_agent: str = 'speakeasy-sdk/python 1.3.0 2.283.1 1.0.0 epilot-entity'
    retry_config: RetryConfig = None
    _hooks: SDKHooks = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
