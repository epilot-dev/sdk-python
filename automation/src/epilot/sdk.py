"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .executions import Executions
from .flows import Flows
from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import components
from typing import Dict

class Epilot:
    r"""Automation API: API Backend for epilot Automation Workflows feature"""
    executions: Executions
    r"""Automation executions"""
    flows: Flows
    r"""Automation flows"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 epilot_auth: str,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param epilot_auth: The epilot_auth required for authentication
        :type epilot_auth: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, components.Security(epilot_auth = epilot_auth))
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.executions = Executions(self.sdk_configuration)
        self.flows = Flows(self.sdk_configuration)
    