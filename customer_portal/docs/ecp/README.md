# ecp

## Overview

ECP

### Available Operations

* [add_end_customer_relation_to_entity](#add_end_customer_relation_to_entity) - addEndCustomerRelationToEntity
* [delete_entity_file](#delete_entity_file) - Delete files from an entity
* [delete_portal_user](#delete_portal_user) - deletePortalUser
* [get_all_contracts](#get_all_contracts) - getAllContracts
* [get_all_opportunities](#get_all_opportunities) - getAllOpportunities
* [get_all_orders](#get_all_orders) - getAllOrders
* [get_contact](#get_contact) - getContact
* [get_contract](#get_contract) - get contract based on id
* [get_entities_by_identifiers](#get_entities_by_identifiers) - getEntitiesByIdentifiers
* [get_opportunity](#get_opportunity) - getOpportunity
* [get_order](#get_order) - getOrder
* [get_organization_settings](#get_organization_settings) - getOrganizationSettings
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_config_by_domain](#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_portal_user](#get_portal_user) - getPortalUser
* [get_schemas](#get_schemas) - getSchemas
* [save_entity_file](#save_entity_file) - Add files to an entity
* [test_auth](#test_auth) - testAuth
* [update_contact](#update_contact) - updateContact
* [update_contract](#update_contract) - Update contract based on id
* [update_opportunity](#update_opportunity) - Update an opportunity based on id
* [update_order](#update_order) - updateOrder
* [update_portal_user](#update_portal_user) - updatePortalUser

## add_end_customer_relation_to_entity

Add EndCustomer Relation To an Entity

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.AddEndCustomerRelationToEntityRequest(
    id='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
    slug='contact',
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
        '12345',
    ],
)

res = s.ecp.delete_entity_file(req, operations.DeleteEntityFileSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.delete_entity_file_200_application_json_object is not None:
    # handle response
```

## delete_portal_user

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.delete_portal_user(operations.DeletePortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.delete_portal_user_200_application_json_string is not None:
    # handle response
```

## get_all_contracts

TODO

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

TODO

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

TODO

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

Get the Contact by id

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

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetContractRequest(
    id='b7392059-2939-46fe-a759-6eb10faaa235',
)

res = s.ecp.get_contract(req, operations.GetContractSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_contract_200_application_json_object is not None:
    # handle response
```

## get_entities_by_identifiers

Get Entities By Identifiers

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetEntitiesByIdentifiersRequest(
    request_body={
        "nobis": 'enim',
    },
    slug='contact',
)

res = s.ecp.get_entities_by_identifiers(req, operations.GetEntitiesByIdentifiersSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_entities_by_identifiers_200_application_json_object is not None:
    # handle response
```

## get_opportunity

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetOpportunityRequest(
    id='955907af-f1a3-4a2f-a946-7739251aa52c',
)

res = s.ecp.get_opportunity(req, operations.GetOpportunitySecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_opportunity_200_application_json_object is not None:
    # handle response
```

## get_order

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetOrderRequest(
    id='3f5ad019-da1f-4fe7-8f09-7b0074f15471',
)

res = s.ecp.get_order(req, operations.GetOrderSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.get_order_200_application_json_object is not None:
    # handle response
```

## get_organization_settings

get organization settings

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_organization_settings(operations.GetOrganizationSettingsSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.organization_settings is not None:
    # handle response
```

## get_portal_config

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetPortalConfigRequest(
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp.get_portal_config(req, operations.GetPortalConfigSecurity(
    epilot_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.portal_config is not None:
    # handle response
```

## get_portal_config_by_domain

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetPortalConfigByDomainRequest(
    domain='example.com',
)

res = s.ecp.get_portal_config_by_domain(req)

if res.portal_config is not None:
    # handle response
```

## get_portal_user

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp.get_portal_user(operations.GetPortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
    # handle response
```

## get_schemas

TODO

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
                '12345',
                '12345',
                '12345',
                '12345',
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
                '12345',
                '12345',
                '12345',
                '12345',
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
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.save_entity_file_200_application_json_object is not None:
    # handle response
```

## test_auth

TODO

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)


res = s.ecp.test_auth()

if res.status_code == 200:
    # handle response
```

## update_contact

Update the contact details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = {
    "quidem": 'molestias',
}

res = s.ecp.update_contact(req, operations.UpdateContactSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
    # handle response
```

## update_contract

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateContractRequest(
    request_body={
        "pariatur": 'modi',
        "praesentium": 'rem',
        "voluptates": 'quasi',
    },
    id='e91e450a-d2ab-4d44-a698-02d502a94bb4',
)

res = s.ecp.update_contract(req, operations.UpdateContractSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_contract_200_application_json_object is not None:
    # handle response
```

## update_opportunity

TODO

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOpportunityRequest(
    request_body={
        "eum": 'non',
        "eligendi": 'sint',
        "aliquid": 'provident',
        "necessitatibus": 'sint',
    },
    id='a3efa77d-fb14-4cd6-aae3-95efb9ba88f3',
)

res = s.ecp.update_opportunity(req, operations.UpdateOpportunitySecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_opportunity_200_application_json_object is not None:
    # handle response
```

## update_order

Update the order details

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.UpdateOrderRequest(
    request_body={
        "nisi": 'vel',
        "natus": 'omnis',
        "molestiae": 'perferendis',
    },
    id='74ba4469-b6e2-4141-9598-90afa563e251',
)

res = s.ecp.update_order(req, operations.UpdateOrderSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
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
    "doloribus": 'debitis',
    "eius": 'maxime',
}

res = s.ecp.update_portal_user(req, operations.UpdatePortalUserSecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
    # handle response
```
