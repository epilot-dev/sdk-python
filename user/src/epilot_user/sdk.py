"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, NoOpLogger
from .utils.retries import RetryConfig
from epilot_user import models, utils
from epilot_user._hooks import SDKHooks
from epilot_user.types import OptionalNullable, UNSET
from epilot_user.user_v1 import UserV1
from epilot_user.user_v2_sdk import UserV2SDK
import httpx
from typing import Any, Callable, Dict, Optional, Union

class Epilot(BaseSDK):
    r"""User API: Manage users in epilot organization(s)

    """
    user_v1: UserV1
    r"""Legacy User API"""
    user_v2: UserV2SDK
    r"""User API V2"""
    def __init__(
        self,
        epilot_auth: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param epilot_auth: The epilot_auth required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = NoOpLogger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."
        
        security: Any = None
        if callable(epilot_auth):
            security = lambda: models.Security(epilot_auth = epilot_auth()) # pylint: disable=unnecessary-lambda-assignment
        else:
            security = models.Security(epilot_auth = epilot_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        BaseSDK.__init__(self, SDKConfiguration(
            client=client,
            async_client=async_client,
            security=security,
            server_url=server_url,
            server_idx=server_idx,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger
        ))

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.user_v1 = UserV1(self.sdk_configuration)
        self.user_v2 = UserV2SDK(self.sdk_configuration)
    
