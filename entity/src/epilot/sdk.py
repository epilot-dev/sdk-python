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
from epilot.models import shared

class Epilot:
    r"""Flexible data layer for epilot Entities.
    
    Use this API configure and access your business objects like Contacts, Opportunities and Products.
    
    [Feature Documentation](https://docs.epilot.io/docs/entities/flexible-entities)
    """
    activity: Activity
    r"""Entity Events"""
    entities: Entities
    r"""CRUD Access for Entities"""
    entity_import: EntityImport
    export: Export
    r"""Export and Import entities via files"""
    relations: Relations
    r"""Entity Relationships"""
    saved_views: SavedViews
    r"""Saved Views for Entities"""
    schemas: Schemas
    r"""Model Entities"""
    taxonomy: Taxonomy
    r"""Entity classification with Taxonomies"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = utils.configure_security_client(client, security)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.activity = Activity(self.sdk_configuration)
        self.entities = Entities(self.sdk_configuration)
        self.entity_import = EntityImport(self.sdk_configuration)
        self.export = Export(self.sdk_configuration)
        self.relations = Relations(self.sdk_configuration)
        self.saved_views = SavedViews(self.sdk_configuration)
        self.schemas = Schemas(self.sdk_configuration)
        self.taxonomy = Taxonomy(self.sdk_configuration)
    