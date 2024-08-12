# Public
(*public*)

## Overview

Public APIs

### Available Operations

* [check_contact_exists](#check_contact_exists) - checkContactExists
* [confirm_user](#confirm_user) - confirmUser
* [confirm_user_with_user_id](#confirm_user_with_user_id) - confirmUserWithUserId
* [create_user](#create_user) - createUser
* [get_portal_config_by_domain](#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_widgets](#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](#user_exists) - userExists

## check_contact_exists

True if contact with given identifiers exists.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.check_contact_exists(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, contact_exists_request={
    "org_id": "728",
    "registration_identifiers": {
        "contact": {
            "email": "john.doe@example.com",
        },
        "contract": {
            "contract_number": "123456",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `contact_exists_request`                                            | [models.ContactExistsRequest](../../models/contactexistsrequest.md) | :heavy_check_mark:                                                  | Request payload                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CheckContactExistsResponseBody](../../models/checkcontactexistsresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,404,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## confirm_user

Confirm a portal user

### Example Usage

```python
from epilot_customer_portal import Epilot

s = Epilot()


s.public.confirm_user(confirmation_link_token="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `confirmation_link_token`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## confirm_user_with_user_id

Confirm a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot()


s.public.confirm_user_with_user_id(id="5da0a718-c822-403d-9f5d-20d4584e0528", org_id="123", origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of portal user id                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Organization ID                                                     | 123                                                                 |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_user

Registers a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.create_user(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, create_user_request={
    "email": "testemail921@yopmail.com",
    "org_id": "728",
    "password": "124n$aAJs*d41h4",
    "contact_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "first_name": "John",
    "last_name": "Doe",
    "registration_identifiers": {
        "contact": {
            "email": "john.doe@example.com",
        },
        "contract": {
            "contract_number": "123456",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `create_user_request`                                               | [models.CreateUserRequest](../../models/createuserrequest.md)       | :heavy_check_mark:                                                  | Portal user payload                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CreateUserResponseBody](../../models/createuserresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_config_by_domain

Retrieves the portal configuration by domain.

### Example Usage

```python
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.get_portal_config_by_domain(domain="example.com")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | example.com                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_public_portal_config

Retrieves the public portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.get_public_portal_config(org_id="12324", origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12324                                                               |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_public_portal_widgets

Retrieves the public widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.get_public_portal_widgets(org_id="123", origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123                                                                 |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## user_exists

Checks whether a user exists in the portal

### Example Usage

```python
from epilot_customer_portal import Epilot

s = Epilot()


res = s.public.user_exists(email="user@example.com", org_id="123")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `email`                                                                                    | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | user@example.com                                                                           |
| `org_id`                                                                                   | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | 123                                                                                        |
| `origin`                                                                                   | [Optional[models.Origin]](../../models/origin.md)                                          | :heavy_minus_sign:                                                                         | Checkes if user exists in the given portal origin. If not provided, checks in all origins. |                                                                                            |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |                                                                                            |


### Response

**[models.UserExistsResponseBody](../../models/userexistsresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
