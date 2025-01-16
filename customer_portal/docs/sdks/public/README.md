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
* [get_public_portal_extension_details](#get_public_portal_extension_details) - getPublicPortalExtensionDetails
* [get_public_portal_widgets](#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](#user_exists) - userExists

## check_contact_exists

True if contact with given identifiers exists.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.check_contact_exists(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, org_id="728", registration_identifiers={
        "contact": {
            "email": "john.doe@example.com",
        },
        "contract": {
            "contract_number": "123456",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `origin`                                                                                          | [models.Origin](../../models/origin.md)                                                           | :heavy_check_mark:                                                                                | Origin of the portal                                                                              |                                                                                                   |
| `org_id`                                                                                          | *str*                                                                                             | :heavy_check_mark:                                                                                | ID of the organization                                                                            | 728                                                                                               |
| `registration_identifiers`                                                                        | Dict[str, Dict[str, *str*]]                                                                       | :heavy_check_mark:                                                                                | Identifier-value pairs per schema to identify a contact of a portal user during the resgistration | {<br/>"contact": {<br/>"email": "john.doe@example.com"<br/>},<br/>"contract": {<br/>"contract_number": "123456"<br/>}<br/>} |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.CheckContactExistsResponseBody](../../models/checkcontactexistsresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 404         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## confirm_user

Confirm a portal user

### Example Usage

```python
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.confirm_user(confirmation_link_token="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `confirmation_link_token`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `use_redirect`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfirmUserResponseBody](../../models/confirmuserresponsebody.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.ConfirmUserPublicResponseBody | 400                                  | application/json                     |
| models.ErrorResp                     | 500                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## confirm_user_with_user_id

Confirm a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    epilot.public.confirm_user_with_user_id(id="5da0a718-c822-403d-9f5d-20d4584e0528", org_id="123", origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## create_user

Registers a portal user

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.create_user(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, email="testemail921@yopmail.com", org_id="728", password="124n$aAJs*d41h4", contact_id="5da0a718-c822-403d-9f5d-20d4584e0528", first_name="John", last_name="Doe", registration_identifiers={
        "contact": {
            "email": "john.doe@example.com",
        },
        "contract": {
            "contract_number": "123456",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                | Example                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `origin`                                                                                                                                                                   | [models.Origin](../../models/origin.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                         | Origin of the portal                                                                                                                                                       |                                                                                                                                                                            |
| `email`                                                                                                                                                                    | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | User's email address                                                                                                                                                       | testemail921@yopmail.com                                                                                                                                                   |
| `org_id`                                                                                                                                                                   | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | ID of the organization                                                                                                                                                     | 728                                                                                                                                                                        |
| `password`                                                                                                                                                                 | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | User's password                                                                                                                                                            | 124n$aAJs*d41h4                                                                                                                                                            |
| `contact_id`                                                                                                                                                               | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Entity ID                                                                                                                                                                  | 5da0a718-c822-403d-9f5d-20d4584e0528                                                                                                                                       |
| `contact_identifiers`                                                                                                                                                      | Dict[str, *str*]                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated. Use registration_identifiers instead. |                                                                                                                                                                            |
| `first_name`                                                                                                                                                               | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | First Name of the portal user                                                                                                                                              | John                                                                                                                                                                       |
| `last_name`                                                                                                                                                                | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Last Name of the portal user                                                                                                                                               | Doe                                                                                                                                                                        |
| `registration_identifiers`                                                                                                                                                 | Dict[str, Dict[str, *str*]]                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                         | Identifier-value pairs per schema to identify a contact of a portal user during the resgistration                                                                          | {<br/>"contact": {<br/>"email": "john.doe@example.com"<br/>},<br/>"contract": {<br/>"contract_number": "123456"<br/>}<br/>}                                                |
| `retries`                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                        |                                                                                                                                                                            |

### Response

**[models.CreateUserResponseBody](../../models/createuserresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400              | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_config_by_domain

Retrieves the portal configuration by domain.

### Example Usage

```python
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.get_portal_config_by_domain(domain="example.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | example.com                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PortalConfig](../../models/portalconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_public_portal_config

Retrieves the public portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.get_public_portal_config(org_id="12324", origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_public_portal_extension_details

Get public extension details shown to end customers and configuring users.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.get_public_portal_extension_details(org_id="12324", origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12324                                                               |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PublicExtensionCapabilities](../../models/publicextensioncapabilities.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_public_portal_widgets

Retrieves the public widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.get_public_portal_widgets(org_id="123", origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403         | application/json |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## user_exists

Checks whether a user exists in the portal

### Example Usage

```python
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.public.user_exists(email="user@example.com", org_id="123")

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |