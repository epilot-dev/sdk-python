# Public
(*.public*)

## Overview

Public APIs

### Available Operations

* [confirm_user](#confirm_user) - confirmUser
* [create_user](#create_user) - createUser
* [get_contact_count](#get_contact_count) - getContactCount
* [get_count_by_email](#get_count_by_email) - getCountByEmail
* [get_portal_config_by_domain](#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_widgets](#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](#user_exists) - userExists

## confirm_user

Confirm a portal user

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.confirm_user(id='5da0a718-c822-403d-9f5d-20d4584e0528', org_id='123', origin=components.Origin.INSTALLER_PORTAL)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | The ID of portal user id                           | 5da0a718-c822-403d-9f5d-20d4584e0528               |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | Organization ID                                    | 123                                                |
| `origin`                                           | [components.Origin](../../models/shared/origin.md) | :heavy_check_mark:                                 | Origin of the portal                               |                                                    |


### Response

**[operations.ConfirmUserResponse](../../models/operations/confirmuserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |

## create_user

Registers a portal user

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.create_user(create_user_request=components.CreateUserRequest(
    contact_id='123456',
    contact_identifiers={
        "key": 'string',
    },
    email='testemail921@yopmail.com',
    first_name='John',
    last_name='Doe',
    org_id='728',
    password='124n$aAJs*d41h4',
    secondary_identifier='123456',
), origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `create_user_request`                                                    | [components.CreateUserRequest](../../models/shared/createuserrequest.md) | :heavy_check_mark:                                                       | Portal user payload                                                      |
| `origin`                                                                 | [components.Origin](../../models/shared/origin.md)                       | :heavy_check_mark:                                                       | Origin of the portal                                                     |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_contact_count

Check existence of contacts.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.get_contact_count(contact_count_request=components.ContactCountRequest(
    contact_identifiers={
        "key": 'string',
    },
    org_id='728',
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `contact_count_request`                                                      | [components.ContactCountRequest](../../models/shared/contactcountrequest.md) | :heavy_check_mark:                                                           | Request payload                                                              |
| `origin`                                                                     | [components.Origin](../../models/shared/origin.md)                           | :heavy_check_mark:                                                           | Origin of the portal                                                         |


### Response

**[operations.GetContactCountResponse](../../models/operations/getcontactcountresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,404,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_count_by_email

Check Contact by email

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.get_count_by_email(email='test@test.com', org_id='123')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `email`            | *str*              | :heavy_check_mark: | N/A                | test@test.com      |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | 123                |


### Response

**[operations.GetCountByEmailResponse](../../models/operations/getcountbyemailresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_portal_config_by_domain

Retrieves the portal configuration by domain.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.get_portal_config_by_domain(domain='example.com')

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `domain`           | *str*              | :heavy_check_mark: | N/A                | example.com        |


### Response

**[operations.GetPortalConfigByDomainResponse](../../models/operations/getportalconfigbydomainresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_public_portal_config

Retrieves the public portal configuration.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.get_public_portal_config(org_id='12324', origin=components.Origin.INSTALLER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                | 12324                                              |
| `origin`                                           | [components.Origin](../../models/shared/origin.md) | :heavy_check_mark:                                 | Origin of the portal                               |                                                    |


### Response

**[operations.GetPublicPortalConfigResponse](../../models/operations/getpublicportalconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |

## get_public_portal_widgets

Retrieves the public widgets of a portal

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.get_public_portal_widgets(org_id='123', origin=components.Origin.END_CUSTOMER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                | 123                                                |
| `origin`                                           | [components.Origin](../../models/shared/origin.md) | :heavy_check_mark:                                 | Origin of the portal                               |                                                    |


### Response

**[operations.GetPublicPortalWidgetsResponse](../../models/operations/getpublicportalwidgetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |

## user_exists

Checks whether a user exists in the portal

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.public.user_exists(email='user@example.com', org_id='123', origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `email`                                                                                    | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | user@example.com                                                                           |
| `org_id`                                                                                   | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | 123                                                                                        |
| `origin`                                                                                   | [Optional[components.Origin]](../../models/shared/origin.md)                               | :heavy_minus_sign:                                                                         | Checkes if user exists in the given portal origin. If not provided, checks in all origins. |                                                                                            |


### Response

**[operations.UserExistsResponse](../../models/operations/userexistsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |
