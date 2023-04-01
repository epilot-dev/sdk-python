"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .activity import Activity
from .entities import Entities
from .export import Export
from .relations import Relations
from .saved_views import SavedViews
from .schemas import Schemas
from .taxonomy import Taxonomy
from epilot.models import shared

SERVERS = [
    "https://entity.sls.epilot.io",
]
"""Contains the list of servers available to the SDK"""

class Epilot:
    r"""Flexible data layer for epilot Entities.
    
    Use this API configure and access your business objects like Contacts, Opportunities and Products.
    
    [Feature Documentation](https://docs.epilot.io/docs/entities/flexible-entities)
    """
    activity: Activity
    r"""Entity Events"""
    entities: Entities
    r"""CRUD Access for Entities"""
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

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.4"
    _gen_version: str = "2.16.7"

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
        self.activity = Activity(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.entities = Entities(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.export = Export(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.relations = Relations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.saved_views = SavedViews(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.schemas = Schemas(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.taxonomy = Taxonomy(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    