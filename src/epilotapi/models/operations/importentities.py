import dataclasses
from typing import Optional
from ..shared import entityimportparams as shared_entityimportparams


@dataclasses.dataclass
class ImportEntitiesQueryParams:
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ImportEntitiesRequest:
    query_params: ImportEntitiesQueryParams = dataclasses.field()
    request: Optional[shared_entityimportparams.EntityImportParams] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ImportEntitiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
