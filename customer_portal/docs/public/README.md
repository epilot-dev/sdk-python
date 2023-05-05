# public

## Overview

Public

### Available Operations

* [activate_user](#activate_user) - activateUser
* [confirm_user](#confirm_user) - confirmUser
* [create_user](#create_user) - creates a user
* [get_count_by_email](#get_count_by_email) - getCountByEmail
* [user_exists](#user_exists) - userExists

## activate_user

Activates the user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)

req = operations.ActivateUserRequest(
    user_activation_payload=shared.UserActivationPayload(
        display_name='Example User',
        password='AKjhdakjsdh@!34',
    ),
    token='corporis',
)

res = s.public.activate_user(req)

if res.status_code == 200:
    # handle response
```

## confirm_user

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)

req = operations.ConfirmUserRequest(
    id='fbb25870-5320-42c7-bd5f-e9b90c28909b',
    org_id='123',
    origin=shared.OriginEnum.END_CUSTOMER_PORTAL,
)

res = s.public.confirm_user(req)

if res.entity_item is not None:
    # handle response
```

## create_user

Creates a user in cognito pool and db item

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateUserRequest(
    request_body=operations.CreateUserRequestBody(
        contact_id='123456',
        email='testemail921@yopmail.com',
        org_id='728',
        password='Pass1234!',
        secondary_identifier='123456',
    ),
    origin=shared.OriginEnum.INSTALLER_PORTAL,
)

res = s.public.create_user(req)

if res.add_portal_resp is not None:
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
        as_customer="YOUR_API_KEY_HERE",
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

## user_exists

Checks whether a user exists in the customer portal

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
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
