# public

## Overview

Public APIs

### Available Operations

* [confirm_user](#confirm_user) - confirmUser
* [create_user](#create_user) - createUser
* [get_count_by_email](#get_count_by_email) - getCountByEmail
* [get_portal_config_by_domain](#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](#get_public_portal_config) - getPublicPortalConfig
* [user_exists](#user_exists) - userExists

## confirm_user

Confirm a portal user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ConfirmUserRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    org_id='123',
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.public.confirm_user(req)

if res.status_code == 200:
    # handle response
```

## create_user

Registers a portal user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateUserRequest(
    create_user_request=shared.CreateUserRequest(
        contact_id='123456',
        email='testemail921@yopmail.com',
        first_name='John',
        last_name='Doe',
        org_id='728',
        password='124n$aAJs*d41h4',
        secondary_identifier='123456',
    ),
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.public.create_user(req)

if res.create_user_201_application_json_object is not None:
    # handle response
```

## get_count_by_email

Check Contact by email

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetCountByEmailRequest(
    email='test@test.com',
    org_id='123',
)

res = s.public.get_count_by_email(req)

if res.get_count_by_email_200_application_json_object is not None:
    # handle response
```

## get_portal_config_by_domain

Retrieves the portal configuration by domain.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetPortalConfigByDomainRequest(
    domain='example.com',
)

res = s.public.get_portal_config_by_domain(req)

if res.portal_config is not None:
    # handle response
```

## get_public_portal_config

Retrieves the public portal configuration.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetPublicPortalConfigRequest(
    org_id='12324',
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.public.get_public_portal_config(req)

if res.portal_config is not None:
    # handle response
```

## user_exists

Checks whether a user exists in the portal

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UserExistsRequest(
    email='user@example.com',
    org_id='123',
)

res = s.public.user_exists(req)

if res.user_exists_200_application_json_object is not None:
    # handle response
```
