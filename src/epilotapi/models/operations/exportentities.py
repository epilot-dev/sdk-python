import dataclasses
from ..shared import entitysearchparams as shared_entitysearchparams
from typing import Optional


@dataclasses.dataclass
class ExportEntitiesQueryParams:
    is_template: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'is_template', 'style': 'form', 'explode': True }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    language: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'language', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ExportEntitiesRequest:
    query_params: ExportEntitiesQueryParams = dataclasses.field()
    request: Optional[shared_entitysearchparams.EntitySearchParams] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ExportEntitiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    