# epilotapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install epilotapi
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilotapi
from epilotapi.models import operations, shared

s = epilotapi.EpilotAPI()
s.config_security(
    security=shared.Security(
        epilot_auth=shared.SchemeEpilotAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    )
)
    
req = operations.AttachActivityRequest(
    path_params=operations.AttachActivityPathParams(
        id="sit",
    ),
    query_params=operations.AttachActivityQueryParams(
        entities=[
            "culpa",
        ],
    ),
)
    
res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations

### Activity

* `attach_activity` - attachActivity
* `create_activity` - createActivity
* `get_activity` - getActivity
* `get_entity_activity_feed` - getEntityActivityFeed

### Entities

* `autocomplete` - autocomplete
* `create_entity` - createEntity
* `delete_entity` - deleteEntity
* `get_entity` - getEntity
* `search_entities` - searchEntities
* `update_entity` - updateEntity
* `upsert_entity` - upsertEntity

### Export

* `export_entities` - exportEntities
* `import_entities` - importEntities

### Journeys

* `create_journey` - createJourney
* `get_journey` - getJourney
* `get_journeys_by_org_id` - getJourneysByOrgId
* `patch_update_journey` - patchUpdateJourney
* `remove_journey` - removeJourney
* `search_journeys` - searchJourneys
* `update_journey` - updateJourney

### Relations

* `add_relations` - addRelations
* `delete_relation` - deleteRelation
* `get_relations` - getRelations
* `update_relation` - updateRelation

### Saved Views

* `create_saved_view` - createSavedView
* `delete_saved_view` - deleteSavedView
* `get_saved_view` - getSavedView
* `list_saved_views` - listSavedViews
* `update_saved_view` - updateSavedView

### Schemas

* `create_new_schema_version` - createNewSchemaVersion
* `delete_schema_by_id` - deleteSchemaById
* `get_schema` - getSchema
* `get_schema_versions` - getSchemaVersions
* `list_schema_blueprints` - listSchemaBlueprints
* `list_schemas` - listSchemas
* `list_taxonomy_classifications_for_schema` - listTaxonomyClassificationsForSchema

### Taxonomy

* `get_taxonomy` - getTaxonomy
* `list_taxonomies` - listTaxonomies
* `taxonomies_classifications_search` - taxonomiesClassificationsSearch
* `taxonomy_autocomplete` - taxonomyAutocomplete
* `update_classifications_for_taxonomy` - updateClassificationsForTaxonomy

### executions

* `cancel_execution` - cancelExecution
* `get_execution` - getExecution
* `get_executions` - getExecutions
* `retrigger_action` - retriggerAction
* `start_execution` - startExecution

### flows

* `create_flow` - createFlow
* `delete_flow` - deleteFlow
* `get_flow` - getFlow
* `put_flow` - putFlow
* `search_flows` - searchFlows

<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
