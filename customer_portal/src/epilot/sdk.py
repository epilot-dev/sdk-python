"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .activity import Activity
from .balance import Balance
from .ecp import Ecp
from .ecp_admin import ECPAdmin
from .public import Public
from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import components
from typing import Dict

class Epilot:
    r"""Portal API: Backend for epilot portals - End Customer Portal & Installer Portal"""
    ecp_admin: ECPAdmin
    r"""APIs defined for a ECP Admin"""
    balance: Balance
    ecp: Ecp
    r"""APIs defined for a portal user"""
    public: Public
    r"""Public APIs"""
    activity: Activity

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: components.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: components.Security
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
        
        
        security_client = utils.configure_security_client(client, security)
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.ecp_admin = ECPAdmin(self.sdk_configuration)
        self.balance = Balance(self.sdk_configuration)
        self.ecp = Ecp(self.sdk_configuration)
        self.public = Public(self.sdk_configuration)
        self.activity = Activity(self.sdk_configuration)
    