# Roles
(*roles*)

## Overview

Manage roles and grants

### Available Operations

* [delete_role](#delete_role) - deleteRole
* [get_role](#get_role) - getRole
* [list_all_roles](#list_all_roles) - listAllRoles
* [list_current_roles](#list_current_roles) - listCurrentRoles
* [put_role](#put_role) - putRole
* [refresh_permissions](#refresh_permissions) - refreshPermissions
* [search_roles](#search_roles) - searchRoles

## delete_role

Delete role by id

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.delete_role(role_id="123:owner")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123:owner                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Role](../../models/role.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_role

Get role by id

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.get_role(role_id="123:owner")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123:owner                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Role](../../models/role.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_all_roles

Returns list of all roles in organization

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.list_all_roles()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListAllRolesResponseBody](../../models/listallrolesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_current_roles

Returns roles and grants assigned to current user

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.list_current_roles()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListCurrentRolesResponseBody](../../models/listcurrentrolesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_role

Create or update role

### Example Usage

```python
import dateutil.parser
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.put_role(role_id="123:owner", role_payload={
    "grants": [

    ],
    "id": "123:owner",
    "name": "Owner",
    "organization_id": "123",
    "slug": "owner",
    "type": epilot_permissions.SchemasUserRoleType.USER_ROLE,
    "expires_at": dateutil.parser.isoparse("2028-07-21T17:32:28Z"),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123:owner                                                           |
| `role_payload`                                                      | [Optional[models.RolePayload]](../../models/rolepayload.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Role](../../models/role.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## refresh_permissions

Makes sure the user has a role in the organization

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.roles.refresh_permissions()

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_roles

Search Roles

### Example Usage

```python
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.search_roles(request={
    "limit": 1,
    "offset": 1,
    "org_ids": [
        "123",
        "456",
    ],
    "query": "Administrator",
    "role_ids": [
        "123:manager",
        "456:owner",
    ],
    "slugs": [
        "manager",
        "owner",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RoleSearchInput](../../models/rolesearchinput.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchRolesResponseBody](../../models/searchrolesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
