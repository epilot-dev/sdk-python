"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .availability_api import AvailabilityAPI
from .cart_api import CartAPI
from .catalog_api import CatalogAPI
from .deprecated import Deprecated
from .order_api import OrderAPI
from epilot.models import shared

SERVERS = [
    "https://pricing-api.sls.epilot.io",
    "https://pricing-api.sls.epilot.io",
]
"""Contains the list of servers available to the SDK"""

class Epilot:
    r"""The `pricing-api` hub sets the foundations for the following Pricing APIs:
    
    ### Order API
    This api enables the management of orders in epilot 360, providing features such as:
     - Automatic calculation of totals and price breakdowns for taxes on the Order entity
     - Product and pricing data validation
    
    ### Shopping Cart API
    Used to interact with a cart during a customer's checkout session, providing:
     - An unified data model to model a Shopping Cart
     - Product and pricing data validation
     - Checkout a cart into an order or quote
    
    ### Catalog API
    Provides a way to query the entire catalog of products and prices.
    
    ### Availability API
    Provides endpoints for querying products availability by a set of predefined dimensions.
    """
    availability_api: AvailabilityAPI
    r"""Provides endpoints for querying products availability by a set of predefined dimensions."""
    cart_api: CartAPI
    r"""Used to interact with a cart during a customer's checkout session, providing:
     - An unified data model to model a Shopping Cart
     - Product and pricing data validation
     - Checkout a cart into an order or quote
    """
    catalog_api: CatalogAPI
    r"""Provides a way to query the entire catalog of products and prices."""
    deprecated: Deprecated
    order_api: OrderAPI
    r"""This api enables the management of orders in epilot 360, providing features such as:
     - Automatic calculation of totals and price breakdowns for taxes on the Order entity
     - Product and pricing data validation
    """

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.0"
    _gen_version: str = "2.17.8"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.availability_api = AvailabilityAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.cart_api = CartAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.catalog_api = CatalogAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.deprecated = Deprecated(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.order_api = OrderAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    