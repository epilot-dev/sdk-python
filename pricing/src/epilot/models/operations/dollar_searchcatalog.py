"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import catalogsearch as shared_catalogsearch
from ..shared import catalogsearchresult as shared_catalogsearchresult
from typing import Any, Optional


@dataclasses.dataclass
class DollarSearchCatalogRequest:
    
    catalog_search: shared_catalogsearch.CatalogSearch = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    x_ivy_org_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Ivy-Org-ID', 'style': 'simple', 'explode': False }})
    r"""The target Organization Id represented by the caller"""  
    

@dataclasses.dataclass
class DollarSearchCatalogResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    catalog_search_result: Optional[shared_catalogsearchresult.CatalogSearchResult] = dataclasses.field(default=None)
    r"""The search result"""  
    error: Optional[Any] = dataclasses.field(default=None)
    r"""Invalid payload"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    