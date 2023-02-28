from __future__ import annotations
import dataclasses
from ..shared import classificationsupdate as shared_classificationsupdate
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclasses.dataclass
class UpdateClassificationsForTaxonomyPathParams:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateClassificationsForTaxonomyRequest:
    path_params: UpdateClassificationsForTaxonomyPathParams = dataclasses.field()
    request: Optional[shared_classificationsupdate.ClassificationsUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateClassificationsForTaxonomy200ApplicationJSON:
    created: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'exclude': lambda f: f is None }})
    deleted: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateClassificationsForTaxonomyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    update_classifications_for_taxonomy_200_application_json_object: Optional[UpdateClassificationsForTaxonomy200ApplicationJSON] = dataclasses.field(default=None)
    