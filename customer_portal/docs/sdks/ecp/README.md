# Ecp
(*ecp*)

## Overview

APIs defined for a portal user

### Available Operations

* [add_end_customer_relation_to_entity](#add_end_customer_relation_to_entity) - addEndCustomerRelationToEntity
* [create_custom_entity_activity](#create_custom_entity_activity) - createCustomEntityActivity
* [delete_entity_file](#delete_entity_file) - deleteEntityFile
* [delete_portal_user](#delete_portal_user) - deletePortalUser
* [get_all_contracts](#get_all_contracts) - getAllContracts
* [get_all_files](#get_all_files) - getAllFiles
* [get_all_opportunities](#get_all_opportunities) - getAllOpportunities
* [get_all_orders](#get_all_orders) - getAllOrders
* [get_billing_events](#get_billing_events) - getBillingEvents
* [get_contact](#get_contact) - getContact
* [get_contract](#get_contract) - getContract
* [get_entities_by_identifiers](#get_entities_by_identifiers) - getEntitiesByIdentifiers
* [get_file_by_id](#get_file_by_id) - getFileById
* [get_files_count_by_entity](#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](#get_opportunity) - getOpportunity
* [get_order](#get_order) - getOrder
* [get_organization_settings](#get_organization_settings) - getOrganizationSettings
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_user](#get_portal_user) - getPortalUser
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_schemas](#get_schemas) - getSchemas
* [save_entity_file](#save_entity_file) - saveEntityFile
* [search_payment_relations_in_entities](#search_payment_relations_in_entities) - searchPaymentRelationsInEntities
* [search_portal_user_entities](#search_portal_user_entities) - searchPortalUserEntities
* [track_file_downloaded](#track_file_downloaded) - trackFileDownloaded
* [trigger_entity_access_event](#trigger_entity_access_event) - triggerEntityAccessEvent
* [update_contact](#update_contact) - updateContact
* [update_contract](#update_contract) - updateContract
* [update_opportunity](#update_opportunity) - updateOpportunity
* [update_order](#update_order) - updateOrder
* [update_portal_user](#update_portal_user) - updatePortalUser
* [validate_cadence_entity_edit_rules](#validate_cadence_entity_edit_rules) - validateCadenceEntityEditRules

## add_end_customer_relation_to_entity

Add portal user relation to an entity

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.add_end_customer_relation_to_entity("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528', slug=components.EntitySlug.CONTACT)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                             | [operations.AddEndCustomerRelationToEntitySecurity](../../models/operations/addendcustomerrelationtoentitysecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |                                                                                                                        |
| `id`                                                                                                                   | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The ID of the Entity                                                                                                   | 5da0a718-c822-403d-9f5d-20d4584e0528                                                                                   |
| `slug`                                                                                                                 | [components.EntitySlug](../../models/components/entityslug.md)                                                         | :heavy_check_mark:                                                                                                     | The slug of an entity                                                                                                  | contact                                                                                                                |


### Response

**[operations.AddEndCustomerRelationToEntityResponse](../../models/operations/addendcustomerrelationtoentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## create_custom_entity_activity

Create a custom activity that can be displayed in activity feed of an entity.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.create_custom_entity_activity("<YOUR_BEARER_TOKEN_HERE>", activity=components.Activity(
    message='{{caller}} did something with {{entity payload.entity.id}}.',
    payload={
        'entity': 'string',
    },
    title='My custom activity',
    type='MyCustomActivity',
), entities=[
    '5da0a718-c822-403d-9f5d-20d4584e0528',
])

if res.activity_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                     | [operations.CreateCustomEntityActivitySecurity](../../models/operations/createcustomentityactivitysecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |
| `activity`                                                                                                     | [Optional[components.Activity]](../../models/components/activity.md)                                           | :heavy_minus_sign:                                                                                             | N/A                                                                                                            |
| `entities`                                                                                                     | List[*str*]                                                                                                    | :heavy_minus_sign:                                                                                             | Comma-separated list of entities which the activity primarily concerns                                         |


### Response

**[operations.CreateCustomEntityActivityResponse](../../models/operations/createcustomentityactivityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete_entity_file

Delete files from an entity

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()

req = components.DeleteEntityFile(
    entity_id='123456',
    entity_type='order',
    file_entity_ids=[
        '12345',
    ],
)

res = s.ecp.delete_entity_file(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.DeleteEntityFile](../../models/components/deleteentityfile.md)                 | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.DeleteEntityFileSecurity](../../models/operations/deleteentityfilesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.DeleteEntityFileResponse](../../models/operations/deleteentityfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorResp    | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## delete_portal_user

Delete the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.delete_portal_user("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.DeletePortalUserSecurity](../../models/operations/deleteportalusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.DeletePortalUserResponse](../../models/operations/deleteportaluserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_all_contracts

Get all contracts for a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_contracts("<YOUR_BEARER_TOKEN_HERE>", from_=0, size=100)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.GetAllContractsSecurity](../../models/operations/getallcontractssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |                                                                                          |
| `from_`                                                                                  | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | N/A                                                                                      | 0                                                                                        |
| `size`                                                                                   | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | N/A                                                                                      | 100                                                                                      |


### Response

**[operations.GetAllContractsResponse](../../models/operations/getallcontractsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_all_files

Fetch all documents under the related entities of a contact

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_files("<YOUR_BEARER_TOKEN_HERE>", from_=0, size=0, entity_ids=[
    '4910096f-000a-4504-bf5a-d3774ec3032a',
    '7c9f8536-6266-42e8-a0de-c60b61aa81a7',
])

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.GetAllFilesSecurity](../../models/operations/getallfilessecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |                                                                                  |
| `from_`                                                                          | *float*                                                                          | :heavy_check_mark:                                                               | N/A                                                                              | 0                                                                                |
| `size`                                                                           | *float*                                                                          | :heavy_check_mark:                                                               | N/A                                                                              | 0                                                                                |
| `entity_ids`                                                                     | List[*str*]                                                                      | :heavy_minus_sign:                                                               | List of entity ids to filter the results                                         | ["4910096f-000a-4504-bf5a-d3774ec3032a","7c9f8536-6266-42e8-a0de-c60b61aa81a7"]  |


### Response

**[operations.GetAllFilesResponse](../../models/operations/getallfilesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_all_opportunities

Get all opportunities of a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_opportunities("<YOUR_BEARER_TOKEN_HERE>", from_=0, size=100)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetAllOpportunitiesSecurity](../../models/operations/getallopportunitiessecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |                                                                                                  |
| `from_`                                                                                          | *Optional[float]*                                                                                | :heavy_minus_sign:                                                                               | N/A                                                                                              | 0                                                                                                |
| `size`                                                                                           | *Optional[float]*                                                                                | :heavy_minus_sign:                                                                               | N/A                                                                                              | 100                                                                                              |


### Response

**[operations.GetAllOpportunitiesResponse](../../models/operations/getallopportunitiesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_all_orders

Get all orders for the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_orders("<YOUR_BEARER_TOKEN_HERE>", from_=0, size=100)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.GetAllOrdersSecurity](../../models/operations/getallorderssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |                                                                                    |
| `from_`                                                                            | *Optional[float]*                                                                  | :heavy_minus_sign:                                                                 | N/A                                                                                | 0                                                                                  |
| `size`                                                                             | *Optional[float]*                                                                  | :heavy_minus_sign:                                                                 | N/A                                                                                | 100                                                                                |


### Response

**[operations.GetAllOrdersResponse](../../models/operations/getallordersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_billing_events

Fetch billing events for a portal user

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_billing_events("<YOUR_BEARER_TOKEN_HERE>", date_after=dateutil.parser.isoparse('2021-09-06T11:20:21.393Z'), date_before=dateutil.parser.isoparse('2022-12-14T11:26:39.960Z'), entity_id='string', event_type=operations.EventType.REIMBURSEMENT)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.GetBillingEventsSecurity](../../models/operations/getbillingeventssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `date_after`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                       | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `date_before`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                       | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `entity_id`                                                                                | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `event_type`                                                                               | [Optional[operations.EventType]](../../models/operations/eventtype.md)                     | :heavy_minus_sign:                                                                         | Type of billing event to filter by                                                         |


### Response

**[operations.GetBillingEventsResponse](../../models/operations/getbillingeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_contact

Retrieves the contact by ID.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_contact("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetContactSecurity](../../models/operations/getcontactsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetContactResponse](../../models/operations/getcontactresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_contract

Get a contract by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_contract("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.GetContractSecurity](../../models/operations/getcontractsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |                                                                                  |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the contract                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                             |


### Response

**[operations.GetContractResponse](../../models/operations/getcontractresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_entities_by_identifiers

Get entities by identifiers by portal user

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.get_entities_by_identifiers("<YOUR_BEARER_TOKEN_HERE>", request_body={
    'key': 'string',
}, slug=components.EntitySlug.CONTACT)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                 | [operations.GetEntitiesByIdentifiersSecurity](../../models/operations/getentitiesbyidentifierssecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |                                                                                                            |
| `request_body`                                                                                             | Dict[str, *Any*]                                                                                           | :heavy_check_mark:                                                                                         | The entities are retrieved successfully.                                                                   |                                                                                                            |
| `slug`                                                                                                     | [components.EntitySlug](../../models/components/entityslug.md)                                             | :heavy_check_mark:                                                                                         | The slug of an entity                                                                                      | contact                                                                                                    |


### Response

**[operations.GetEntitiesByIdentifiersResponse](../../models/operations/getentitiesbyidentifiersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,403,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_file_by_id

Fetch a document with ID

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_file_by_id("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.GetFileByIDSecurity](../../models/operations/getfilebyidsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |                                                                                  |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The Id of a file                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                             |


### Response

**[operations.GetFileByIDResponse](../../models/operations/getfilebyidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_files_count_by_entity

Fetch file counts for all ECP user related entities

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_files_count_by_entity("<YOUR_BEARER_TOKEN_HERE>")

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.GetFilesCountByEntitySecurity](../../models/operations/getfilescountbyentitysecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetFilesCountByEntityResponse](../../models/operations/getfilescountbyentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_opportunity

Get an opportunity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_opportunity("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.GetOpportunitySecurity](../../models/operations/getopportunitysecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |                                                                                        |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The ID of opportunity                                                                  | 5da0a718-c822-403d-9f5d-20d4584e0528                                                   |


### Response

**[operations.GetOpportunityResponse](../../models/operations/getopportunityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_order

Get an order by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_order("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.GetOrderSecurity](../../models/operations/getordersecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |                                                                            |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | The ID of order                                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                                       |


### Response

**[operations.GetOrderResponse](../../models/operations/getorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_organization_settings

Retrieves the organization settings.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_organization_settings("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `security`                                                                                               | [operations.GetOrganizationSettingsSecurity](../../models/operations/getorganizationsettingssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetOrganizationSettingsResponse](../../models/operations/getorganizationsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.get_portal_config(operations.GetPortalConfigSecurity(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.GetPortalConfigSecurity](../../models/operations/getportalconfigsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `origin`                                                                                 | [Optional[components.Origin]](../../models/components/origin.md)                         | :heavy_minus_sign:                                                                       | Origin of the portal                                                                     |


### Response

**[operations.GetPortalConfigResponse](../../models/operations/getportalconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_portal_user

Get the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_portal_user("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.GetPortalUserSecurity](../../models/operations/getportalusersecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetPortalUserResponse](../../models/operations/getportaluserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.get_portal_widgets(operations.GetPortalWidgetsSecurity(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.GetPortalWidgetsSecurity](../../models/operations/getportalwidgetssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `origin`                                                                                   | [Optional[components.Origin]](../../models/components/origin.md)                           | :heavy_minus_sign:                                                                         | Origin of the portal                                                                       |


### Response

**[operations.GetPortalWidgetsResponse](../../models/operations/getportalwidgetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_schemas

Retrieves the schemas.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_schemas("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetSchemasSecurity](../../models/operations/getschemassecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetSchemasResponse](../../models/operations/getschemasresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## save_entity_file

Add files to an entity

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()

req = components.SaveEntityFile(
    entity_id='123456',
    entity_type='order',
    files=[
        components.Files(
            tags=[
                'string',
            ],
            document_type='12345',
            file_entity_id='12345',
            filename='12345',
            s3ref=components.S3ref(
                bucket='12345',
                key='12345',
            ),
        ),
    ],
)

res = s.ecp.save_entity_file(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.SaveEntityFile](../../models/components/saveentityfile.md)                 | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.SaveEntityFileSecurity](../../models/operations/saveentityfilesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.SaveEntityFileResponse](../../models/operations/saveentityfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorResp    | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## search_payment_relations_in_entities

Search for entities that have the payment relation with the given payment id


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.search_payment_relations_in_entities(id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | Entity id                            | 5da0a718-c822-403d-9f5d-20d4584e0528 |


### Response

**[operations.SearchPaymentRelationsInEntitiesResponse](../../models/operations/searchpaymentrelationsinentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## search_portal_user_entities

Search all entities of a portal user

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()

req = components.EntitySearchParams(
    fields=[
        '_id',
        '_title',
        'first_name',
    ],
    slug=components.EntitySlug.CONTACT,
    sort='_created_at:desc',
)

res = s.ecp.search_portal_user_entities(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.EntitySearchParams](../../models/components/entitysearchparams.md)                             | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.SearchPortalUserEntitiesSecurity](../../models/operations/searchportaluserentitiessecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.SearchPortalUserEntitiesResponse](../../models/operations/searchportaluserentitiesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## track_file_downloaded

Track that user has downloaded a file

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.track_file_downloaded("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.TrackFileDownloadedSecurity](../../models/operations/trackfiledownloadedsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |                                                                                                  |
| `id`                                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | The Id of a file                                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                                             |


### Response

**[operations.TrackFileDownloadedResponse](../../models/operations/trackfiledownloadedresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## trigger_entity_access_event

Trigger entity access event for a portal user

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp.trigger_entity_access_event("<YOUR_BEARER_TOKEN_HERE>", entity_id='1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e', origin=components.Origin.END_CUSTOMER_PORTAL, schema='contract')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                 | [operations.TriggerEntityAccessEventSecurity](../../models/operations/triggerentityaccesseventsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |                                                                                                            |
| `entity_id`                                                                                                | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Entity ID                                                                                                  | 1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e                                                                       |
| `origin`                                                                                                   | [Optional[components.Origin]](../../models/components/origin.md)                                           | :heavy_minus_sign:                                                                                         | Portal origin                                                                                              |                                                                                                            |
| `schema`                                                                                                   | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Entity schema                                                                                              | contract                                                                                                   |


### Response

**[operations.TriggerEntityAccessEventResponse](../../models/operations/triggerentityaccesseventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_contact

Updates the contact details.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    'key': 'string',
}

res = s.ecp.update_contact(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [Dict[str, Any]](../../models/.md)                                                   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdateContactSecurity](../../models/operations/updatecontactsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdateContactResponse](../../models/operations/updatecontactresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResp                 | 401,404,500                      | application/json                 |
| errors.UpdateContactResponseBody | 403                              | application/json                 |
| errors.SDKError                  | 400-600                          | */*                              |

## update_contract

Update a contract by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.update_contract("<YOUR_BEARER_TOKEN_HERE>", request_body={
    'key': 'string',
}, id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.UpdateContractSecurity](../../models/operations/updatecontractsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |                                                                                        |
| `request_body`                                                                         | Dict[str, *Any*]                                                                       | :heavy_check_mark:                                                                     | Requested contract body to update                                                      |                                                                                        |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The ID of the contract                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                                   |


### Response

**[operations.UpdateContractResponse](../../models/operations/updatecontractresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorResp                  | 401,404,500                       | application/json                  |
| errors.UpdateContractResponseBody | 403                               | application/json                  |
| errors.SDKError                   | 400-600                           | */*                               |

## update_opportunity

Update an opportunity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.update_opportunity("<YOUR_BEARER_TOKEN_HERE>", request_body={
    'key': 'string',
}, id='5da0a718-c822-403d-9f5d-20d4584e0528')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.UpdateOpportunitySecurity](../../models/operations/updateopportunitysecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |                                                                                              |
| `request_body`                                                                               | Dict[str, *Any*]                                                                             | :heavy_check_mark:                                                                           | Requested opportunity body to update                                                         |                                                                                              |
| `id`                                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The ID of opportunity                                                                        | 5da0a718-c822-403d-9f5d-20d4584e0528                                                         |


### Response

**[operations.UpdateOpportunityResponse](../../models/operations/updateopportunityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## update_order

Update an order by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.update_order("<YOUR_BEARER_TOKEN_HERE>", id='5da0a718-c822-403d-9f5d-20d4584e0528', request_body={
    'key': 'string',
})

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.UpdateOrderSecurity](../../models/operations/updateordersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |                                                                                  |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The ID of order                                                                  | 5da0a718-c822-403d-9f5d-20d4584e0528                                             |
| `request_body`                                                                   | Dict[str, *Any*]                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |


### Response

**[operations.UpdateOrderResponse](../../models/operations/updateorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 400-600          | */*              |

## update_portal_user

Update the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    'key': 'string',
}

res = s.ecp.update_portal_user(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [Dict[str, Any]](../../models/.md)                                                         | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdatePortalUserSecurity](../../models/operations/updateportalusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdatePortalUserResponse](../../models/operations/updateportaluserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## validate_cadence_entity_edit_rules

Validate if cadence rule is valid for an entity


### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.validate_cadence_entity_edit_rules(id='5da0a718-c822-403d-9f5d-20d4584e0528', slug=components.EntitySlug.CONTACT, attribute=dateutil.parser.isoparse('2023-04-17T01:10:16.547Z'))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Entity id                                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                                 |
| `slug`                                                               | [components.EntitySlug](../../models/components/entityslug.md)       | :heavy_check_mark:                                                   | Entity Type                                                          | contact                                                              |
| `attribute`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Get activities after this timestamp                                  |                                                                      |


### Response

**[operations.ValidateCadenceEntityEditRulesResponse](../../models/operations/validatecadenceentityeditrulesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
