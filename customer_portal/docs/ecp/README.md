# ecp

## Overview

APIs defined for a portal user

### Available Operations

* [add_end_customer_relation_to_entity](#add_end_customer_relation_to_entity) - addEndCustomerRelationToEntity
* [delete_entity_file](#delete_entity_file) - deleteEntityFile
* [delete_portal_user](#delete_portal_user) - deletePortalUser
* [get_all_contracts](#get_all_contracts) - getAllContracts
* [get_all_opportunities](#get_all_opportunities) - getAllOpportunities
* [get_all_orders](#get_all_orders) - getAllOrders
* [get_contact](#get_contact) - getContact
* [get_contract](#get_contract) - getContract
* [get_entities_by_identifiers](#get_entities_by_identifiers) - getEntitiesByIdentifiers
* [get_opportunity](#get_opportunity) - getOpportunity
* [get_order](#get_order) - getOrder
* [get_organization_settings](#get_organization_settings) - getOrganizationSettings
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_user](#get_portal_user) - getPortalUser
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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.add_end_customer_relation_to_entity_200_application_json_object is not None:
    # handle response
```

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
        '12345',
        '12345',
    ],
)

res = s.ecp.delete_entity_file(req, operations.DeleteEntityFileSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.delete_entity_file_202_application_json_object is not None:
    # handle response
```

## delete_portal_user

Delete the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.delete_portal_user(operations.DeletePortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.delete_portal_user_200_application_json_object is not None:
    # handle response
```

## get_all_contracts

Get all contracts for a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_contracts(operations.GetAllContractsSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_all_contracts_200_application_json_object is not None:
    # handle response
```

## get_all_opportunities

Get all opportunities of a portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_opportunities(operations.GetAllOpportunitiesSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_all_opportunities_200_application_json_object is not None:
    # handle response
```

## get_all_orders

Get all orders for the portal user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_all_orders(operations.GetAllOrdersSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_all_orders_200_application_json_object is not None:
    # handle response
```

## get_contact

Retrieves the contact by ID.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_contact(operations.GetContactSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_contact_200_application_json_object is not None:
    # handle response
```

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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_contract_200_application_json_object is not None:
    # handle response
```

## get_entities_by_identifiers

Get entities by identifiers by portal user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetEntitiesByIdentifiersRequest(
    request_body={
        "distinctio": 'quibusdam',
        "unde": 'nulla',
        "corrupti": 'illum',
    },
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp.get_entities_by_identifiers(req, operations.GetEntitiesByIdentifiersSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_entities_by_identifiers_200_application_json_object is not None:
    # handle response
```

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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_opportunity_200_application_json_object is not None:
    # handle response
```

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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_order_200_application_json_object is not None:
    # handle response
```

## get_organization_settings

Retrieves the organization settings.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_organization_settings(operations.GetOrganizationSettingsSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_organization_settings_200_application_json_object is not None:
    # handle response
```

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetPortalConfigRequest(
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp.get_portal_config(req, operations.GetPortalConfigSecurity(
    epilot_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.portal_config is not None:
    # handle response
```

## get_portal_user

Get the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_portal_user(operations.GetPortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_portal_user_200_application_json_object is not None:
    # handle response
```

## get_schemas

Retrieves the schemas.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_schemas(operations.GetSchemasSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_schemas_200_application_json_object is not None:
    # handle response
```

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
                'suscipit',
                'iure',
                'magnam',
            ],
            access_control=shared.SaveEntityFileFilesAccessControl.PUBLIC_READ,
            document_type='12345',
            file_entity_id='12345',
            filename='12345',
            s3ref=shared.SaveEntityFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
        shared.SaveEntityFileFiles(
            tags=[
                'delectus',
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
        shared.SaveEntityFileFiles(
            tags=[
                'molestiae',
                'minus',
            ],
            access_control=shared.SaveEntityFileFilesAccessControl.PUBLIC_READ,
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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.save_entity_file_201_application_json_object is not None:
    # handle response
```

## update_contact

Updates the contact details.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    "iusto": 'excepturi',
    "nisi": 'recusandae',
    "temporibus": 'ab',
}

res = s.ecp.update_contact(req, operations.UpdateContactSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_contact_200_application_json_object is not None:
    # handle response
```

## update_contract

Update a contract by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateContractRequest(
    request_body={
        "veritatis": 'deserunt',
        "perferendis": 'ipsam',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_contract(req, operations.UpdateContractSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_contract_200_application_json_object is not None:
    # handle response
```

## update_opportunity

Update an opportunity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOpportunityRequest(
    request_body={
        "sapiente": 'quo',
        "odit": 'at',
        "at": 'maiores',
        "molestiae": 'quod',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_opportunity(req, operations.UpdateOpportunitySecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_opportunity_200_application_json_object is not None:
    # handle response
```

## update_order

Update an order by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOrderRequest(
    request_body={
        "esse": 'totam',
        "porro": 'dolorum',
        "dicta": 'nam',
        "officia": 'occaecati',
    },
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
)

res = s.ecp.update_order(req, operations.UpdateOrderSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_order_200_application_json_object is not None:
    # handle response
```

## update_portal_user

Update the portal user details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    "deleniti": 'hic',
}

res = s.ecp.update_portal_user(req, operations.UpdatePortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_portal_user_200_application_json_object is not None:
    # handle response
```
