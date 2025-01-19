# Ecp
(*ecp*)

## Overview

APIs defined for a portal user

### Available Operations

* [add_contract_by_identifiers](#add_contract_by_identifiers) - addContractByIdentifiers
* [create_custom_entity_activity](#create_custom_entity_activity) - createCustomEntityActivity
* [create_meter_reading](#create_meter_reading) - Create Meter Reading
* [delete_entity_file](#delete_entity_file) - deleteEntityFile
* [delete_portal_user](#delete_portal_user) - deletePortalUser
* [get_all_contracts](#get_all_contracts) - getAllContracts
* [get_all_files](#get_all_files) - getAllFiles
* [get_all_opportunities](#get_all_opportunities) - getAllOpportunities
* [get_all_orders](#get_all_orders) - getAllOrders
* [get_billing_events](#get_billing_events) - getBillingEvents
* [get_consumption](#get_consumption) - Get Consumption
* [get_contact](#get_contact) - getContact
* [get_contract](#get_contract) - getContract
* [get_costs](#get_costs) - Get Costs
* [get_external_links](#get_external_links) - getExternalLinks
* [get_file_by_id](#get_file_by_id) - getFileById
* [get_files_count_by_entity](#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](#get_opportunity) - getOpportunity
* [get_order](#get_order) - getOrder
* [get_organization_settings](#get_organization_settings) - getOrganizationSettings
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_user](#get_portal_user) - getPortalUser
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_prices](#get_prices) - Get Prices
* [get_resolved_external_link](#get_resolved_external_link) - getResolvedExternalLink
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

Self-assign contract(s) by pre-configured identifiers.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.add_contract_by_identifiers(request={
        "contract": {
            "contract_number": "123456",
        },
        "meter": {
            "meter_number": "123456",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Dict[str, str]]](../../models/.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddContractByIdentifiersResponseBody](../../models/addcontractbyidentifiersresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.ErrorResp                               | 400, 401, 403                                  | application/json                               |
| models.AddContractByIdentifiersECPResponseBody | 409                                            | application/json                               |
| models.ErrorResp                               | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## create_custom_entity_activity

Create a custom activity that can be displayed in activity feed of an entity.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.create_custom_entity_activity()

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## create_meter_reading

Inserts a new meter reading.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.create_meter_reading(meter_id="5da0a718-c822-403d-9f5d-20d4584e0528", source=epilot_customer_portal.Source.ERP, value=240, counter_id="5da0a718-c822-403d-9f5d-20d4584e0528", read_by="John Doe", reason="Storing the feed-in record", timestamp="2022-10-10T00:00:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `meter_id`                                                                                   | *str*                                                                                        | :heavy_check_mark:                                                                           | Entity ID                                                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                                         |
| `source`                                                                                     | [models.Source](../../models/source.md)                                                      | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |
| `value`                                                                                      | *float*                                                                                      | :heavy_check_mark:                                                                           | The reading value of the meter                                                               | 240                                                                                          |
| `override_plausibility`                                                                      | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Override plausibility check                                                                  |                                                                                              |
| `counter_id`                                                                                 | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Entity ID                                                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                                         |
| `direction`                                                                                  | [Optional[models.Direction]](../../models/direction.md)                                      | :heavy_minus_sign:                                                                           | N/A                                                                                          |                                                                                              |
| `read_by`                                                                                    | *OptionalNullable[str]*                                                                      | :heavy_minus_sign:                                                                           | The person who recorded the reading                                                          | John Doe                                                                                     |
| `reason`                                                                                     | *OptionalNullable[str]*                                                                      | :heavy_minus_sign:                                                                           | The reason for recording the reading                                                         | Storing the feed-in record                                                                   |
| `status`                                                                                     | [OptionalNullable[models.ReadingStatus]](../../models/readingstatus.md)                      | :heavy_minus_sign:                                                                           | N/A                                                                                          |                                                                                              |
| `timestamp`                                                                                  | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | If the value is not provided, the system will be set with the time the request is processed. | 2022-10-10 00:00:00 +0000 UTC                                                                |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[models.CreateMeterReadingResponseBody](../../models/createmeterreadingresponsebody.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.CreateMeterReadingECPResponseBody | 400                                      | application/json                         |
| models.ErrorResp                         | 401, 403                                 | application/json                         |
| models.ErrorResp                         | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## delete_entity_file

Delete files from an entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.delete_entity_file(entity_id="5da0a718-c822-403d-9f5d-20d4584e0528", entity_type="order", file_entity_ids=[
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entity_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `entity_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Entity type                                                         | order                                                               |
| `file_entity_ids`                                                   | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of file entity IDs                                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteEntityFileResponseBody](../../models/deleteentityfileresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 400, 401, 403, 404 | application/json   |
| models.ErrorResp   | 500                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## delete_portal_user

Delete the portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.delete_portal_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletePortalUserResponseBody](../../models/deleteportaluserresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_all_contracts

Get all contracts for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_all_contracts(from_=0, size=100)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_all_files

Fetch all documents under the related entities of a contact

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_all_files(from_=0, size=0, entity_ids=[
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ])

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_all_opportunities

Get all opportunities of a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_all_opportunities(from_=0, size=100)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_all_orders

Get all orders for the portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_all_orders(from_=0, size=100)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_billing_events

Fetch billing events for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_billing_events(entity_id=[
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ], from_=0, size=100, sort="due_date:asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `date_after`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `date_before`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `entity_id`                                                          | List[*str*]                                                          | :heavy_minus_sign:                                                   | Entity ID to filter billing events by                                |                                                                      |
| `event_type`                                                         | [Optional[models.EventType]](../../models/eventtype.md)              | :heavy_minus_sign:                                                   | Type of billing event to filter by                                   |                                                                      |
| `from_`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  | 0                                                                    |
| `paid`                                                               | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `size`                                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  | 100                                                                  |
| `sort`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  | due_date:asc                                                         |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.GetBillingEventsResponseBody](../../models/getbillingeventsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_consumption

Get energy consumption data between a given time period.

### Example Usage

```python
import dateutil.parser
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_consumption(extension_id="<id>", from_=dateutil.parser.isoparse("2024-05-12T18:38:28.810Z"), hook_id="<id>", interval=epilot_customer_portal.Interval.P1_M, meter_id="<id>", to=dateutil.parser.isoparse("2024-10-13T20:40:01.754Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `extension_id`                                                                                                                  | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | Extension ID for consumption data.                                                                                              |
| `from_`                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                            | :heavy_check_mark:                                                                                                              | Start date for consumption data (ISO 8601 format).                                                                              |
| `hook_id`                                                                                                                       | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | Hook ID for consumption data.                                                                                                   |
| `interval`                                                                                                                      | [models.Interval](../../models/interval.md)                                                                                     | :heavy_check_mark:                                                                                                              | Interval between consumption data points (e.g., PT15M for 15 minutes, PT1H for hourly). Not all intervals have to be supported. |
| `meter_id`                                                                                                                      | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | Meter ID for consumption data.                                                                                                  |
| `to`                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                            | :heavy_check_mark:                                                                                                              | End date for consumption data (ISO 8601 format).                                                                                |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.GetConsumptionResponseBody](../../models/getconsumptionresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_contact

Retrieves the contact of the logged in user.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_contact()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetContactResponseBody](../../models/getcontactresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_contract

Get a contract by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_contract(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the contract                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetContractResponseBody](../../models/getcontractresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_costs

Get energy cost data between a given time period.

### Example Usage

```python
import dateutil.parser
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_costs(extension_id="<id>", from_=dateutil.parser.isoparse("2023-02-07T07:43:34.088Z"), hook_id="<id>", interval=epilot_customer_portal.QueryParamInterval.P1_D, meter_id="<id>", to=dateutil.parser.isoparse("2025-06-10T07:17:02.092Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `extension_id`                                                                                                           | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Extension ID for cost data.                                                                                              |
| `from_`                                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                     | :heavy_check_mark:                                                                                                       | Start date for cost data (ISO 8601 format).                                                                              |
| `hook_id`                                                                                                                | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Hook ID for cost data.                                                                                                   |
| `interval`                                                                                                               | [models.QueryParamInterval](../../models/queryparaminterval.md)                                                          | :heavy_check_mark:                                                                                                       | Interval between cost data points (e.g., PT15M for 15 minutes, PT1H for hourly). Not all intervals have to be supported. |
| `meter_id`                                                                                                               | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Meter ID for cost data.                                                                                                  |
| `to`                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                     | :heavy_check_mark:                                                                                                       | End date for cost data (ISO 8601 format).                                                                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetCostsResponseBody](../../models/getcostsresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_external_links

Retrieves the portal configuration external links.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_external_links(contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.ExternalLink]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_file_by_id

Fetch a document with ID

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_file_by_id(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of a file                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetFileByIDResponseBody](../../models/getfilebyidresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_files_count_by_entity

Fetch file counts for all ECP user related entities

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_files_count_by_entity()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.EntityFileCount]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_opportunity

Get an opportunity by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_opportunity(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of opportunity                                               | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOpportunityResponseBody](../../models/getopportunityresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_order

Get an order by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_order(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of order                                                     | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOrderResponseBody](../../models/getorderresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_organization_settings

Retrieves the organization settings.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_organization_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOrganizationSettingsResponseBody](../../models/getorganizationsettingsresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_portal_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PortalConfig](../../models/portalconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_user

Get the portal user details

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_portal_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPortalUserResponseBody](../../models/getportaluserresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_portal_widgets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_prices

Get energy prices data between a given time period.

### Example Usage

```python
import dateutil.parser
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_prices(extension_id="<id>", from_=dateutil.parser.isoparse("2023-07-16T08:39:13.009Z"), hook_id="<id>", interval=epilot_customer_portal.GetPricesQueryParamInterval.PT15_M, meter_id="<id>", to=dateutil.parser.isoparse("2025-08-14T14:51:12.268Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `extension_id`                                                                                                            | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Extension ID for price data.                                                                                              |
| `from_`                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                      | :heavy_check_mark:                                                                                                        | Start date for price data (ISO 8601 format).                                                                              |
| `hook_id`                                                                                                                 | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Hook ID for price data.                                                                                                   |
| `interval`                                                                                                                | [models.GetPricesQueryParamInterval](../../models/getpricesqueryparaminterval.md)                                         | :heavy_check_mark:                                                                                                        | Interval between price data points (e.g., PT15M for 15 minutes, PT1H for hourly). Not all intervals have to be supported. |
| `meter_id`                                                                                                                | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Meter ID for price data.                                                                                                  |
| `to`                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                      | :heavy_check_mark:                                                                                                        | End date for price data (ISO 8601 format).                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.GetPricesResponseBody](../../models/getpricesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_resolved_external_link

Retrieves a resolved portal external link.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_resolved_external_link(id="5da0a718-c822-403d-9f5d-20d4584e0528", contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the External Link                                             | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ExternalLink](../../models/externallink.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_schemas

Retrieves the schemas.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_schemas()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSchemasResponseBody](../../models/getschemasresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_search_results_for_opportunities

Get all opportunity with the given serached attributes

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_search_results_for_opportunities(from_=0, size=1000, purposes=[
        "5da0a718-c822-403d-9f5d-20d4584e0528",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 1000                                                                |
| `addresses`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `customers`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `purposes`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `workflows`                                                         | List[List[[models.Workflows](../../models/workflows.md)]]           | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSearchResultsForOpportunitiesResponseBody](../../models/getsearchresultsforopportunitiesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_searchable_attributes_for_opportunities

Get all opportunity searchable attributes for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.get_searchable_attributes_for_opportunities(from_=0, size=1000)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## post_order_acceptance

Accept/decline an offer by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.post_order_acceptance(id="5da0a718-c822-403d-9f5d-20d4584e0528", decision=epilot_customer_portal.Decision.DECLINE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of order                                                     | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `decision`                                                          | [models.Decision](../../models/decision.md)                         | :heavy_check_mark:                                                  | Acceptance decision                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PostOrderAcceptanceResponseBody](../../models/postorderacceptanceresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 401, 403, 404, 409 | application/json   |
| models.ErrorResp   | 500                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## revoke_token

Revokes all of the access tokens for the given Refresh Token.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.revoke_token(refresh_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 | Example                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `refresh_token`                                                                                                                                             | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | Refresh Token to be revoked                                                                                                                                 | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |                                                                                                                                                             |

### Response

**[models.RevokeTokenResponseBody](../../models/revoketokenresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## save_entity_file

Add files to an entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.save_entity_file(entity_id="5da0a718-c822-403d-9f5d-20d4584e0528", entity_type="order", files=[
        {
            "filename": "document.pdf",
            "s3ref": {
                "bucket": "12345",
                "key": "12345",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entity_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `entity_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Entity type                                                         | order                                                               |
| `files`                                                             | List[[models.Files](../../models/files.md)]                         | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SaveEntityFileResponseBody](../../models/saveentityfileresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 400, 401, 403, 404 | application/json   |
| models.ErrorResp   | 500                | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## search_payment_relations_in_entities

Search for entities that have the payment relation with the given payment id


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.search_payment_relations_in_entities(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Entity id                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SearchPaymentRelationsInEntitiesResponseBody](../../models/searchpaymentrelationsinentitiesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## search_portal_user_entities

Search all entities of a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.search_portal_user_entities(request={
        "slug": epilot_customer_portal.EntitySlug.CONTACT,
        "fields": [
            "_id",
            "_title",
            "first_name",
        ],
        "sort": "_created_at:desc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EntitySearchParams](../../models/entitysearchparams.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchPortalUserEntitiesResponseBody](../../models/searchportaluserentitiesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## track_file_downloaded

Track that user has downloaded a file

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.track_file_downloaded(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of a file                                                    | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TrackFileDownloadedResponseBody](../../models/trackfiledownloadedresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## trigger_entity_access_event

Trigger entity access event for a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.trigger_entity_access_event(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, schema="contract", entity_id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_contact

Updates the contact details.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_contact()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Any]](../../models/.md)                                  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateContactResponseBody](../../models/updatecontactresponsebody.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ErrorResp                    | 401, 404                            | application/json                    |
| models.UpdateContactECPResponseBody | 403                                 | application/json                    |
| models.ErrorResp                    | 500                                 | application/json                    |
| models.APIError                     | 4XX, 5XX                            | \*/\*                               |

## update_contract

Update a contract by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_contract(id="5da0a718-c822-403d-9f5d-20d4584e0528", request_body={

    })

    # Handle response
    print(res)

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

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.ErrorResp                     | 401, 404                             | application/json                     |
| models.UpdateContractECPResponseBody | 403                                  | application/json                     |
| models.ErrorResp                     | 500                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## update_opportunity

Update an opportunity by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_opportunity(id="5da0a718-c822-403d-9f5d-20d4584e0528", request_body={
        "key": "<value>",
        "key1": "<value>",
    })

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_order

Update an order by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_order(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 404    | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_portal_user

Update the portal user details

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_portal_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, Any]](../../models/.md)                                  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdatePortalUserResponseBody](../../models/updateportaluserresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_portal_user_email

Update portal user email

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_portal_user_email(email="john@doe.com", password="XPF599YfftQdi1n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | New email address of the portal user                                | john@doe.com                                                        |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Password of the portal user for confirmation                        |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdatePortalUserEmailResponseBody](../../models/updateportaluseremailresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_workflow_step_as_done

Update a workflow step as done

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.update_workflow_step_as_done(step_id="q1d6vcbsqvn", workflow_id="0bjwcxc827t")

    # Handle response
    print(res)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## validate_cadence_entity_edit_rules

Validate if cadence rule is valid for an entity


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp.validate_cadence_entity_edit_rules(id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT)

    # Handle response
    print(res)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## validate_token

Validates Portal Token is valid. Pass the token via Authorization Header.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.ecp.validate_token()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |