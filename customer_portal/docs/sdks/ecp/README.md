# Ecp
(*ecp*)

## Overview

APIs defined for a portal user

### Available Operations

* [add_contract_by_identifiers](#add_contract_by_identifiers) - addContractByIdentifiers
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
* [get_external_links](#get_external_links) - getExternalLinks
* [get_file_by_id](#get_file_by_id) - getFileById
* [get_files_count_by_entity](#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](#get_opportunity) - getOpportunity
* [get_order](#get_order) - getOrder
* [get_organization_settings](#get_organization_settings) - getOrganizationSettings
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_user](#get_portal_user) - getPortalUser
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_schemas](#get_schemas) - getSchemas
* [get_search_results_for_opportunities](#get_search_results_for_opportunities) - getSearchResultsForOpportunities
* [get_searchable_attributes_for_opportunities](#get_searchable_attributes_for_opportunities) - getSearchableAttributesForOpportunities
* [post_order_acceptance](#post_order_acceptance) - postOrderAcceptance
* [revoke_token](#revoke_token) - revokeToken
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
* [update_portal_user_email](#update_portal_user_email) - updatePortalUserEmail
* [update_workflow_step_as_done](#update_workflow_step_as_done) - updateWorkflowStepAsDone
* [validate_cadence_entity_edit_rules](#validate_cadence_entity_edit_rules) - validateCadenceEntityEditRules
* [validate_token](#validate_token) - validateToken

## add_contract_by_identifiers

Self-assign contract by pre-configured identifiers.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.add_contract_by_identifiers(request={
    "key": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Any]](../../models/.md)                                  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.AddContractByIdentifiersResponseBody](../../models/addcontractbyidentifiersresponsebody.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.ErrorResp                               | 400,401,403,500                                | application/json                               |
| models.AddContractByIdentifiersECPResponseBody | 409                                            | application/json                               |
| models.SDKError                                | 4xx-5xx                                        | */*                                            |

## add_end_customer_relation_to_entity

Add portal user relation to an entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.add_end_customer_relation_to_entity(id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the Entity                                                | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `slug`                                                              | [models.EntitySlug](../../models/entityslug.md)                     | :heavy_check_mark:                                                  | The slug of an entity                                               | contact                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AddEndCustomerRelationToEntityResponseBody](../../models/addendcustomerrelationtoentityresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_custom_entity_activity

Create a custom activity that can be displayed in activity feed of an entity.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.create_custom_entity_activity()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `entities`                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                             | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Comma-separated list of entities which the activity primarily concerns. Deprecated - ignored as the list of entities is automatically determined now. |
| `request_body`                                                                                                                                                                                                                                                                 | [Optional[models.CreateCustomEntityActivityRequestBody]](../../models/createcustomentityactivityrequestbody.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |


### Response

**[models.ActivityItem](../../models/activityitem.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## delete_entity_file

Delete files from an entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.delete_entity_file(request={
    "entity_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "entity_type": "order",
    "file_entity_ids": [
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteEntityFile](../../models/deleteentityfile.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.DeleteEntityFileResponseBody](../../models/deleteentityfileresponsebody.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorResp    | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## delete_portal_user

Delete the portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.delete_portal_user()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.DeletePortalUserResponseBody](../../models/deleteportaluserresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_all_contracts

Get all contracts for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_all_contracts(from_=0, size=100)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 100                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetAllContractsResponseBody](../../models/getallcontractsresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_all_files

Fetch all documents under the related entities of a contact

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_all_files(from_=0, size=0, entity_ids=[
    "4910096f-000a-4504-bf5a-d3774ec3032a",
    "7c9f8536-6266-42e8-a0de-c60b61aa81a7",
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `from_`                                                                            | *float*                                                                            | :heavy_check_mark:                                                                 | N/A                                                                                | 0                                                                                  |
| `size`                                                                             | *float*                                                                            | :heavy_check_mark:                                                                 | N/A                                                                                | 0                                                                                  |
| `entity_ids`                                                                       | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | List of entity ids to filter the results                                           | [<br/>"4910096f-000a-4504-bf5a-d3774ec3032a",<br/>"7c9f8536-6266-42e8-a0de-c60b61aa81a7"<br/>] |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |


### Response

**[models.GetAllFilesResponseBody](../../models/getallfilesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_all_opportunities

Get all opportunities of a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_all_opportunities(from_=0, size=100)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 100                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetAllOpportunitiesResponseBody](../../models/getallopportunitiesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_all_orders

Get all orders for the portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_all_orders(from_=0, size=100)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 100                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetAllOrdersResponseBody](../../models/getallordersresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_billing_events

Fetch billing events for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_billing_events(request={
    "entity_id": [
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ],
    "from_": 0,
    "size": 100,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetBillingEventsRequest](../../models/getbillingeventsrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |


### Response

**[models.GetBillingEventsResponseBody](../../models/getbillingeventsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_contact

Retrieves the contact by ID.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_contact()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetContactResponseBody](../../models/getcontactresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_contract

Get a contract by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_contract(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the contract                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetContractResponseBody](../../models/getcontractresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_external_links

Retrieves the portal configuration external links.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_external_links(contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[List[models.JourneyActions]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_file_by_id

Fetch a document with ID

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_file_by_id(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of a file                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetFileByIDResponseBody](../../models/getfilebyidresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_files_count_by_entity

Fetch file counts for all ECP user related entities

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_files_count_by_entity()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.EntityFileCount]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_opportunity

Get an opportunity by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_opportunity(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of opportunity                                               | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetOpportunityResponseBody](../../models/getopportunityresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_order

Get an order by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_order(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of order                                                     | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetOrderResponseBody](../../models/getorderresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_organization_settings

Retrieves the organization settings.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_organization_settings()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetOrganizationSettingsResponseBody](../../models/getorganizationsettingsresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_portal_config()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_user

Get the portal user details

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_portal_user()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetPortalUserResponseBody](../../models/getportaluserresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_portal_widgets()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_schemas

Retrieves the schemas.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_schemas()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetSchemasResponseBody](../../models/getschemasresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_search_results_for_opportunities

Get all opportunity with the given serached attributes

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_search_results_for_opportunities(request_body={
    "purposes": [
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ],
}, from_=0, size=1000)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                    | [models.GetSearchResultsForOpportunitiesRequestBody](../../models/getsearchresultsforopportunitiesrequestbody.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `from_`                                                                                                           | *Optional[float]*                                                                                                 | :heavy_minus_sign:                                                                                                | N/A                                                                                                               | 0                                                                                                                 |
| `size`                                                                                                            | *Optional[float]*                                                                                                 | :heavy_minus_sign:                                                                                                | N/A                                                                                                               | 1000                                                                                                              |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |


### Response

**[models.GetSearchResultsForOpportunitiesResponseBody](../../models/getsearchresultsforopportunitiesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_searchable_attributes_for_opportunities

Get all opportunity searchable attributes for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.get_searchable_attributes_for_opportunities(from_=0, size=1000)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 1000                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetSearchableAttributesForOpportunitiesResponseBody](../../models/getsearchableattributesforopportunitiesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## post_order_acceptance

Accept/decline an offer by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.post_order_acceptance(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | The ID of order                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                      |
| `acceptance_decision`                                                     | [Optional[models.AcceptanceDecision]](../../models/acceptancedecision.md) | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |


### Response

**[models.PostOrderAcceptanceResponseBody](../../models/postorderacceptanceresponsebody.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorResp    | 401,403,404,409,500 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## revoke_token

Revokes all of the access tokens for the given Refresh Token.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.revoke_token(request={
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RevokeTokenRequestBody](../../models/revoketokenrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |


### Response

**[models.RevokeTokenResponseBody](../../models/revoketokenresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## save_entity_file

Add files to an entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.save_entity_file(request={
    "entity_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "entity_type": "order",
    "files": [
        {
            "filename": "document.pdf",
            "s3ref": {
                "bucket": "12345",
                "key": "12345",
            },
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SaveEntityFile](../../models/saveentityfile.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SaveEntityFileResponseBody](../../models/saveentityfileresponsebody.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorResp    | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## search_payment_relations_in_entities

Search for entities that have the payment relation with the given payment id


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.search_payment_relations_in_entities(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Entity id                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.SearchPaymentRelationsInEntitiesResponseBody](../../models/searchpaymentrelationsinentitiesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_portal_user_entities

Search all entities of a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.search_portal_user_entities(request={
    "slug": epilot_customer_portal.EntitySlug.CONTACT,
    "fields": [
        "_id",
        "_title",
        "first_name",
    ],
    "sort": "_created_at:desc",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EntitySearchParams](../../models/entitysearchparams.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchPortalUserEntitiesResponseBody](../../models/searchportaluserentitiesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## track_file_downloaded

Track that user has downloaded a file

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.track_file_downloaded(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of a file                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.TrackFileDownloadedResponseBody](../../models/trackfiledownloadedresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## trigger_entity_access_event

Trigger entity access event for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.trigger_entity_access_event(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, schema="contract", entity_id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Portal origin                                                       |                                                                     |
| `schema_`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Entity schema                                                       | contract                                                            |
| `entity_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.TriggerEntityAccessEventResponseBody](../../models/triggerentityaccesseventresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_contact

Updates the contact details.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_contact()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Any]](../../models/.md)                                  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpdateContactResponseBody](../../models/updatecontactresponsebody.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ErrorResp                    | 401,404,500                         | application/json                    |
| models.UpdateContactECPResponseBody | 403                                 | application/json                    |
| models.SDKError                     | 4xx-5xx                             | */*                                 |

## update_contract

Update a contract by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_contract(id="5da0a718-c822-403d-9f5d-20d4584e0528", request_body={
    "key": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the contract                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | Requested contract body to update                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UpdateContractResponseBody](../../models/updatecontractresponsebody.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.ErrorResp                     | 401,404,500                          | application/json                     |
| models.UpdateContractECPResponseBody | 403                                  | application/json                     |
| models.SDKError                      | 4xx-5xx                              | */*                                  |

## update_opportunity

Update an opportunity by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_opportunity(id="5da0a718-c822-403d-9f5d-20d4584e0528", request_body={
    "key": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of opportunity                                               | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | Requested opportunity body to update                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UpdateOpportunityResponseBody](../../models/updateopportunityresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_order

Update an order by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_order(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of order                                                     | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UpdateOrderResponseBody](../../models/updateorderresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_portal_user

Update the portal user details

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_portal_user()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Any]](../../models/.md)                                  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpdatePortalUserResponseBody](../../models/updateportaluserresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_portal_user_email

Update portal user email

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_portal_user_email(request={
    "email": "john@doe.com",
    "password": "XnP3YEFSAB569k9",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.UpdatePortalUserEmailRequestBody](../../models/updateportaluseremailrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |


### Response

**[models.UpdatePortalUserEmailResponseBody](../../models/updateportaluseremailresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_workflow_step_as_done

Update a workflow step as done

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.update_workflow_step_as_done(step_id="q1d6vcbsqvn", workflow_id="0bjwcxc827t")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | q1d6vcbsqvn                                                         |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 0bjwcxc827t                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[Dict[str, Any]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## validate_cadence_entity_edit_rules

Validate if cadence rule is valid for an entity


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp.validate_cadence_entity_edit_rules(id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Entity id                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `slug`                                                              | [models.EntitySlug](../../models/entityslug.md)                     | :heavy_check_mark:                                                  | Entity Type                                                         | contact                                                             |
| `attribute`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Get activities after this timestamp                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ValidateCadenceEntityEditRulesResponseBody](../../models/validatecadenceentityeditrulesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## validate_token

Validates Portal Token is valid. Pass the token via Authorization Header.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.ecp.validate_token()

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
