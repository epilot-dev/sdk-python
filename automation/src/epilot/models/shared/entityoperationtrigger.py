"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import diffadded as shared_diffadded
from ..shared import diffdeleted as shared_diffdeleted
from ..shared import diffupdated as shared_diffupdated
from ..shared import entityoperation as shared_entityoperation
from ..shared import filterconditiononevent as shared_filterconditiononevent
from ..shared import orcondition as shared_orcondition
from ..shared import orcondition1 as shared_orcondition1
from ..shared import orconditionfordiff as shared_orconditionfordiff
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTriggerConfigurationFilterConfigActivity:
    type: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Filter on activity type. If not specified, all activities will be matched on execution.
    Example:
      1. Filter the events when an entity is updated from portal
        ```
          { 
            \"activity\":{
              \"type\": [\"EntityUpdatedFromPortal\"]
            }
          }
        ```
      2. Filter the events when either a doc is uploaded/removed on an entity from a portal
        ```
          { 
            \"activity\":{
              \"type\": [\"DocUploadedFromPortal\", \"DocRemovedFromPortal\"]
            }
          }
        ```
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTriggerConfigurationFilterConfigOperationDiff2:
    r"""Diff to it's prior state when an entity is updated"""
    added: Optional[Union[shared_orcondition.OrCondition, Dict[str, List[Union[str, shared_equalsignorecasecondition.EqualsIgnoreCaseCondition, shared_anythingbutcondition.AnythingButCondition, shared_numericcondition.NumericCondition, shared_existscondition.ExistsCondition, shared_prefixcondition.PrefixCondition, shared_suffixcondition.SuffixCondition]]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('added'), 'exclude': lambda f: f is None }})
    deleted: Optional[Union[shared_orcondition.OrCondition, Dict[str, List[Union[str, shared_equalsignorecasecondition.EqualsIgnoreCaseCondition, shared_anythingbutcondition.AnythingButCondition, shared_numericcondition.NumericCondition, shared_existscondition.ExistsCondition, shared_prefixcondition.PrefixCondition, shared_suffixcondition.SuffixCondition]]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[Union[shared_orcondition.OrCondition, Dict[str, List[Union[str, shared_equalsignorecasecondition.EqualsIgnoreCaseCondition, shared_anythingbutcondition.AnythingButCondition, shared_numericcondition.NumericCondition, shared_existscondition.ExistsCondition, shared_prefixcondition.PrefixCondition, shared_suffixcondition.SuffixCondition]]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class EntityOperationTriggerConfigurationFilterConfigOperationDiff:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTriggerConfigurationFilterConfigOperation:
    diff: Optional[Union[shared_orconditionfordiff.OrConditionForDiff, EntityOperationTriggerConfigurationFilterConfigOperationDiff2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('diff'), 'exclude': lambda f: f is None }})
    operation: Optional[List[shared_entityoperation.EntityOperation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation'), 'exclude': lambda f: f is None }})
    r"""Filter on operation type. If not specified, all operations will be matched on execution.
    Example:
      1. Filter all the createEntity/updateEntity operations 
      ```
        { 
          \"operation\":{
            \"operation\": [\"createEntity\", \"updateEntity\"]
          }
        }
      ```
    """
    payload: Optional[Union[shared_orcondition1.OrCondition1, Dict[str, List[Union[str, shared_equalsignorecasecondition.EqualsIgnoreCaseCondition, shared_anythingbutcondition.AnythingButCondition, shared_numericcondition.NumericCondition, shared_existscondition.ExistsCondition, shared_prefixcondition.PrefixCondition, shared_suffixcondition.SuffixCondition]]]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTriggerConfigurationFilterConfig:
    activity: Optional[EntityOperationTriggerConfigurationFilterConfigActivity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity'), 'exclude': lambda f: f is None }})
    operation: Optional[EntityOperationTriggerConfigurationFilterConfigOperation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTriggerConfiguration:
    exclude_activities: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exclude_activities'), 'exclude': lambda f: f is None }})
    filter_config: Optional[EntityOperationTriggerConfigurationFilterConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter_config'), 'exclude': lambda f: f is None }})
    include_activities: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_activities'), 'exclude': lambda f: f is None }})
    operations: Optional[List[shared_entityoperation.EntityOperation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations'), 'exclude': lambda f: f is None }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    


class EntityOperationTriggerType(str, Enum):
    ENTITY_OPERATION = 'entity_operation'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationTrigger:
    r"""- If provides filter_config, executes an automation based on the filtered configuration when an entity event occurs.
    - The conditions on a filter follows the event bridge patterns - `https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html`
      | Comparison             | Example                                             | Rule syntax                                              |
      |------------------------|-----------------------------------------------------|----------------------------------------------------------|
      | Null                   | first_name is null                                  | `\"first_name\": [ null ]`                                 |
      | Empty                  | last_name is empty                                  | `\"last_name\": [\"\"]`                                      |
      | Equals                 | email is \"j.doe@email.com\"                          | `\"email\": [ \"j.doe@email.com\" ]`                         |
      | Equals (ignore case)   | first_name is \"John\"                                | `\"first_name\": [ { \"equals-ignore-case\": \"john\" } ]`     |
      | And                    | fist_name is \"John\" and last_name is \"Doe\"          | `\"first_name\": [ \"John\" ], \"last_name\": [\"Doe\"]`         |
      | Or                     | PaymentType is \"Invoice\" or \"SEPA\"                  | `\"PaymentType\": [ \"invoice\", \"sepa\"]`                    |
      | Or (multiple fields)   | first_name is \"John\", or last_name is \"Doe\".        | `\"$or\": [ { \"first_name\": [ \"John\" ] }, { \"last_name\": [ \"Doe\" ] } ]` |
      | Not                    | status is anything but \"cancelled\"                  | `\"status\": [ { \"anything-but\": [ \"cancelled\" ] } ]`      |
      | Numeric (equals)       | Price is 100                                        | `\"Price\": [ { \"numeric\": [ \"=\", 100 ] } ]`               |
      | Numeric (range)        | Price is more than 10, and less than or equal to 20 | `\"Price\": [ { \"numeric\": [ \">\", 10, \"<=\", 20 ] } ]`      |
      | Exists                 | ProductName exists                                  | `\"ProductName\": [ { \"exists\": true } ]`                  |
      | Does not exist         | ProductName does not exist                          | `\"ProductName\": [ { \"exists\": false } ]`                 |
      | Begins with            | OpportunityNumber starts with OPP-                  | `\"opportunity_number\": [ { \"prefix\": \"OPP-\" } ]`         |
      | Ends with              | FileName ends with a .png extension                 | `\"filename\": [ { \"suffix\": \".png\" } ]`                   |
      - To run the execution on all update events
        ```
          {
            \"type\": \"filter_entity_event\",
            \"configuration\": {
              \"operation\": {
                \"operation\": [\"updateEntity\"]
              }
            }
          }
        ```
      - To run the execution only when the updates are from a portal user
        ```
          {
            \"type\": \"filter_entity_event\",
            \"configuration\": {
              \"operation\": {
                \"operation\": [\"updateEntity\"]
              },
              \"activity\": {
                \"type\": \"EntityUpdatedFromPortal\"
              }
            }
          }
        ```
      - To run the execution only when there is an update on a specific attribute
        ```
          Only starts the automation when the email on a contact is changed
          {
            \"type\": \"filter_entity_event\",
            \"configuration\": {
              \"operation\": {
                \"operation\": [\"updateEntity\"],
                \"payload\": {
                  \"_schema\": [\"contact\"]
                },
                \"diff\": {
                  \"updated\": {
                    \"email\": [{ \"exists\": true }]
                  }
                }
              }
            }
          }
        ```
        - To run the execution only when a specific attribute is altered(created/updated/deleted)
          ```
            Only starts the automation when a price is altered on a contract
            {
              \"type\": \"filter_entity_event\",
              \"configuration\": {
                \"operation\": {
                  \"payload\": {
                    \"_schema\": [\"contract\"]
                  },
                  \"diff\": {
                    // Whether he first_name has been added, updated, or removed
                    $or: [
                      {
                        'added.first_name': [{ exists: true }]
                      },
                      {
                        'updated.first_name': [{ exists: true }]
                      },
                      {
                        'deleted.first_name': [{ exists: true }]
                      }
                    ]
                  }
                }
              }
            }
          ```
        - To run the execution if an attribute is changed from one state to another
          ```
            Only starts the automation when the order status changes from `open_for_acceptance` to `placed`
            {
              \"type\": \"filter_entity_event\",
              \"configuration\": {
                \"operation\": {
                  \"operation\": [\"updateEntity\"],
                  \"payload\": {
                    \"_schema\": [\"order\"],
                    \"status\": [\"placed\"]
                  },
                  \"diff\": {
                    \"updated\": {
                      \"status\": [\"open_for_acceptance\"]
                    }
                  }
                }
              }
            }
          ```
    """
    configuration: EntityOperationTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    type: EntityOperationTriggerType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

