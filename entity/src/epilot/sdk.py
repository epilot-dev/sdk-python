"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .activity import Activity
from .entities import Entities
from .entity_import import EntityImport
from .export import Export
from .relations import Relations
from .saved_views import SavedViews
from .schemas import Schemas
from .sdkconfiguration import SDKConfiguration
from .taxonomy import Taxonomy
from epilot import utils
from epilot._hooks import SDKHooks
from epilot.models import components
from typing import Callable, Dict, Optional, Union

class Epilot:
    r"""Entity API: Flexible data layer for epilot Entities.

    Use this API configure and access your business objects like Contacts, Opportunities and Products.

    [Feature Documentation](https://docs.epilot.io/docs/entities/flexible-entities)
    """
    activity: Activity
    r"""Entity Events"""
    taxonomy: Taxonomy
    r"""Entity classification with Taxonomies"""
    schemas: Schemas
    r"""Model Entities"""
    saved_views: SavedViews
    r"""Saved Views for Entities"""
    entities: Entities
    r"""CRUD Access for Entities"""
    relations: Relations
    r"""Entity Relationships"""
    export: Export
    r"""Export and Import entities via files"""
    entity_import: EntityImport

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[components.Security,Callable[[], components.Security]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[utils.RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[components.Security,Callable[[], components.Security]]
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

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.activity = Activity(self.sdk_configuration)
        self.taxonomy = Taxonomy(self.sdk_configuration)
        self.schemas = Schemas(self.sdk_configuration)
        self.saved_views = SavedViews(self.sdk_configuration)
        self.entities = Entities(self.sdk_configuration)
        self.relations = Relations(self.sdk_configuration)
        self.export = Export(self.sdk_configuration)
        self.entity_import = EntityImport(self.sdk_configuration)
