import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import entityschemaitem as shared_entityschemaitem


@dataclasses.dataclass
class GetSchemaVersionsPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class GetSchemaVersions200ApplicationJSON:
    drafts: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('drafts') }})
    versions: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('versions') }})
    

@dataclasses.dataclass
class GetSchemaVersionsRequest:
    path_params: GetSchemaVersionsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSchemaVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_schema_versions_200_application_json_object: Optional[GetSchemaVersions200ApplicationJSON] = dataclasses.field(default=None)
    
