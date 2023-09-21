# Ecp

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
* [update_contact](#update_contact) - updateContact
* [update_contract](#update_contract) - updateContract
* [update_opportunity](#update_opportunity) - updateOpportunity
* [update_order](#update_order) - updateOrder
* [update_portal_user](#update_portal_user) - updatePortalUser

## add_end_customer_relation_to_entity

Add portal user relation to an entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.AddEndCustomerRelationToEntityRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp.add_end_customer_relation_to_entity(req, operations.AddEndCustomerRelationToEntitySecurity(
    portal_auth="",
))

if res.add_end_customer_relation_to_entity_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.AddEndCustomerRelationToEntityRequest](../../models/operations/addendcustomerrelationtoentityrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.AddEndCustomerRelationToEntitySecurity](../../models/operations/addendcustomerrelationtoentitysecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.AddEndCustomerRelationToEntityResponse](../../models/operations/addendcustomerrelationtoentityresponse.md)**


## create_custom_entity_activity

Create a custom activity that can be displayed in activity feed of an entity.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.CreateCustomEntityActivityRequest(
    activity=shared.Activity(
        message='{{caller}} did something with {{entity payload.entity.id}}.',
        payload={
            "corrupti": 'provident',
        },
        title='My custom activity',
        type='MyCustomActivity',
    ),
    entities=[
        '5da0a718-c822-403d-9f5d-20d4584e0528',
    ],
)

res = s.ecp.create_custom_entity_activity(req, operations.CreateCustomEntityActivitySecurity(
    portal_auth="",
))

if res.activity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateCustomEntityActivityRequest](../../models/operations/createcustomentityactivityrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.CreateCustomEntityActivitySecurity](../../models/operations/createcustomentityactivitysecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.CreateCustomEntityActivityResponse](../../models/operations/createcustomentityactivityresponse.md)**


## delete_entity_file

Delete files from an entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = shared.DeleteEntityFile(
    entity_id='123456',
    entity_type='order',
    file_entity_ids=[
        '12345',
    ],
)

res = s.ecp.delete_entity_file(req, operations.DeleteEntityFileSecurity(
    portal_auth="",
))

if res.delete_entity_file_202_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.DeleteEntityFile](../../models/shared/deleteentityfile.md)                         | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.DeleteEntityFileSecurity](../../models/operations/deleteentityfilesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.DeleteEntityFileResponse](../../models/operations/deleteentityfileresponse.md)**


## delete_portal_user

Delete the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.delete_portal_user(operations.DeletePortalUserSecurity(
    portal_auth="",
))

if res.delete_portal_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.DeletePortalUserSecurity](../../models/operations/deleteportalusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.DeletePortalUserResponse](../../models/operations/deleteportaluserresponse.md)**


## get_all_contracts

Get all contracts for a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_contracts(operations.GetAllContractsSecurity(
    portal_auth="",
))

if res.get_all_contracts_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.GetAllContractsSecurity](../../models/operations/getallcontractssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetAllContractsResponse](../../models/operations/getallcontractsresponse.md)**


## get_all_files

Fetch all documents under the related entities of a contact

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetAllFilesRequest(
    entity_ids=[
        'distinctio',
    ],
    from_=0,
    size=0,
)

res = s.ecp.get_all_files(req, operations.GetAllFilesSecurity(
    portal_auth="",
))

if res.get_all_files_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetAllFilesRequest](../../models/operations/getallfilesrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetAllFilesSecurity](../../models/operations/getallfilessecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetAllFilesResponse](../../models/operations/getallfilesresponse.md)**


## get_all_opportunities

Get all opportunities of a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_opportunities(operations.GetAllOpportunitiesSecurity(
    portal_auth="",
))

if res.get_all_opportunities_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetAllOpportunitiesSecurity](../../models/operations/getallopportunitiessecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAllOpportunitiesResponse](../../models/operations/getallopportunitiesresponse.md)**


## get_all_orders

Get all orders for the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_orders(operations.GetAllOrdersSecurity(
    portal_auth="",
))

if res.get_all_orders_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.GetAllOrdersSecurity](../../models/operations/getallorderssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.GetAllOrdersResponse](../../models/operations/getallordersresponse.md)**


## get_contact

Retrieves the contact by ID.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_contact(operations.GetContactSecurity(
    portal_auth="",
))

if res.get_contact_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetContactSecurity](../../models/operations/getcontactsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetContactResponse](../../models/operations/getcontactresponse.md)**


## get_contract

Get a contract by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetContractRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.get_contract(req, operations.GetContractSecurity(
    portal_auth="",
))

if res.get_contract_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetContractRequest](../../models/operations/getcontractrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetContractSecurity](../../models/operations/getcontractsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetContractResponse](../../models/operations/getcontractresponse.md)**


## get_entities_by_identifiers

Get entities by identifiers by portal user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetEntitiesByIdentifiersRequest(
    request_body={
        "quibusdam": 'unde',
    },
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp.get_entities_by_identifiers(req, operations.GetEntitiesByIdentifiersSecurity(
    portal_auth="",
))

if res.get_entities_by_identifiers_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetEntitiesByIdentifiersRequest](../../models/operations/getentitiesbyidentifiersrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetEntitiesByIdentifiersSecurity](../../models/operations/getentitiesbyidentifierssecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetEntitiesByIdentifiersResponse](../../models/operations/getentitiesbyidentifiersresponse.md)**


## get_file_by_id

Fetch a document with ID

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetFileByIDRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.get_file_by_id(req, operations.GetFileByIDSecurity(
    portal_auth="",
))

if res.get_file_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetFileByIDRequest](../../models/operations/getfilebyidrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetFileByIDSecurity](../../models/operations/getfilebyidsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetFileByIDResponse](../../models/operations/getfilebyidresponse.md)**


## get_files_count_by_entity

Fetch file counts for all ECP user related entities

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_files_count_by_entity(operations.GetFilesCountByEntitySecurity(
    portal_auth="",
))

if res.entity_file_counts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.GetFilesCountByEntitySecurity](../../models/operations/getfilescountbyentitysecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetFilesCountByEntityResponse](../../models/operations/getfilescountbyentityresponse.md)**


## get_opportunity

Get an opportunity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetOpportunityRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.get_opportunity(req, operations.GetOpportunitySecurity(
    portal_auth="",
))

if res.get_opportunity_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetOpportunityRequest](../../models/operations/getopportunityrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetOpportunitySecurity](../../models/operations/getopportunitysecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetOpportunityResponse](../../models/operations/getopportunityresponse.md)**


## get_order

Get an order by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetOrderRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.get_order(req, operations.GetOrderSecurity(
    portal_auth="",
))

if res.get_order_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetOrderRequest](../../models/operations/getorderrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.GetOrderSecurity](../../models/operations/getordersecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.GetOrderResponse](../../models/operations/getorderresponse.md)**


## get_organization_settings

Retrieves the organization settings.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_organization_settings(operations.GetOrganizationSettingsSecurity(
    portal_auth="",
))

if res.get_organization_settings_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `security`                                                                                               | [operations.GetOrganizationSettingsSecurity](../../models/operations/getorganizationsettingssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetOrganizationSettingsResponse](../../models/operations/getorganizationsettingsresponse.md)**


## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetPortalConfigRequest(
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp.get_portal_config(req, operations.GetPortalConfigSecurity(
    epilot_auth="",
))

if res.portal_config is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPortalConfigRequest](../../models/operations/getportalconfigrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetPortalConfigSecurity](../../models/operations/getportalconfigsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetPortalConfigResponse](../../models/operations/getportalconfigresponse.md)**


## get_portal_user

Get the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_portal_user(operations.GetPortalUserSecurity(
    portal_auth="",
))

if res.get_portal_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.GetPortalUserSecurity](../../models/operations/getportalusersecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetPortalUserResponse](../../models/operations/getportaluserresponse.md)**


## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetPortalWidgetsRequest(
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp.get_portal_widgets(req, operations.GetPortalWidgetsSecurity(
    epilot_auth="",
))

if res.upsert_portal_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPortalWidgetsRequest](../../models/operations/getportalwidgetsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.GetPortalWidgetsSecurity](../../models/operations/getportalwidgetssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.GetPortalWidgetsResponse](../../models/operations/getportalwidgetsresponse.md)**


## get_schemas

Retrieves the schemas.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_schemas(operations.GetSchemasSecurity(
    portal_auth="",
))

if res.get_schemas_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetSchemasSecurity](../../models/operations/getschemassecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetSchemasResponse](../../models/operations/getschemasresponse.md)**


## save_entity_file

Add files to an entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = shared.SaveEntityFile(
    entity_id='123456',
    entity_type='order',
    files=[
        shared.SaveEntityFileFiles(
            tags=[
                'illum',
            ],
            access_control=shared.SaveEntityFileFilesAccessControl.PRIVATE,
            document_type='12345',
            file_entity_id='12345',
            filename='12345',
            s3ref=shared.SaveEntityFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
    ],
)

res = s.ecp.save_entity_file(req, operations.SaveEntityFileSecurity(
    portal_auth="",
))

if res.save_entity_file_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.SaveEntityFile](../../models/shared/saveentityfile.md)                         | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.SaveEntityFileSecurity](../../models/operations/saveentityfilesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.SaveEntityFileResponse](../../models/operations/saveentityfileresponse.md)**


## update_contact

Updates the contact details.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    "error": 'deserunt',
}

res = s.ecp.update_contact(req, operations.UpdateContactSecurity(
    portal_auth="",
))

if res.update_contact_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [dict[str, Any]](../../models//.md)                                                  | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdateContactSecurity](../../models/operations/updatecontactsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdateContactResponse](../../models/operations/updatecontactresponse.md)**


## update_contract

Update a contract by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateContractRequest(
    request_body={
        "suscipit": 'iure',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_contract(req, operations.UpdateContractSecurity(
    portal_auth="",
))

if res.update_contract_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateContractRequest](../../models/operations/updatecontractrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.UpdateContractSecurity](../../models/operations/updatecontractsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.UpdateContractResponse](../../models/operations/updatecontractresponse.md)**


## update_opportunity

Update an opportunity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOpportunityRequest(
    request_body={
        "magnam": 'debitis',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_opportunity(req, operations.UpdateOpportunitySecurity(
    portal_auth="",
))

if res.update_opportunity_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateOpportunityRequest](../../models/operations/updateopportunityrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateOpportunitySecurity](../../models/operations/updateopportunitysecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateOpportunityResponse](../../models/operations/updateopportunityresponse.md)**


## update_order

Update an order by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOrderRequest(
    request_body={
        "ipsa": 'delectus',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_order(req, operations.UpdateOrderSecurity(
    portal_auth="",
))

if res.update_order_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateOrderRequest](../../models/operations/updateorderrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.UpdateOrderSecurity](../../models/operations/updateordersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.UpdateOrderResponse](../../models/operations/updateorderresponse.md)**


## update_portal_user

Update the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    "tempora": 'suscipit',
}

res = s.ecp.update_portal_user(req, operations.UpdatePortalUserSecurity(
    portal_auth="",
))

if res.update_portal_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [dict[str, Any]](../../models//.md)                                                        | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdatePortalUserSecurity](../../models/operations/updateportalusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdatePortalUserResponse](../../models/operations/updateportaluserresponse.md)**

