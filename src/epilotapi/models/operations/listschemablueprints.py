from __future__ import annotations
import dataclasses
from ..shared import entityschemaitem as shared_entityschemaitem
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSchemaBlueprints200ApplicationJSON:
    results: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListSchemaBlueprintsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_schema_blueprints_200_application_json_object: Optional[ListSchemaBlueprints200ApplicationJSON] = dataclasses.field(default=None)
    