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
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.delete_role(role_id='123:owner')

if res.role is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `role_id`          | *str*              | :heavy_check_mark: | N/A                | 123:owner          |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_role

Get role by id

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.get_role(role_id='123:owner')

if res.role is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `role_id`          | *str*              | :heavy_check_mark: | N/A                | 123:owner          |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_all_roles

Returns list of all roles in organization

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.list_all_roles()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ListAllRolesResponse](../../models/operations/listallrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_current_roles

Returns roles and grants assigned to current user

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.list_current_roles()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ListCurrentRolesResponse](../../models/operations/listcurrentrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_role

Create or update role

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.put_role(role_id='123:owner', role_payload=components.One(
    grants=[
        components.GrantWithDependencies(
            action='entity-read',
            conditions=[
                components.EqualsCondition(
                    attribute='workflows.primary.task_name',
                    operation=components.Operation.EQUALS,
                    values=[
                        'Qualification',
                    ],
                ),
            ],
            dependencies=[
                components.Grant(
                    action='entity-read',
                    conditions=[
                        components.EqualsCondition(
                            attribute='workflows.primary.task_name',
                            operation=components.Operation.EQUALS,
                            values=[
                                'Qualification',
                            ],
                        ),
                    ],
                    resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
                ),
            ],
            resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
        ),
    ],
    id='123:owner',
    name='Owner',
    organization_id='123',
    slug='owner',
    type=components.RolePayloadType.USER_ROLE,
    expires_at=dateutil.parser.isoparse('2028-07-21T17:32:28Z'),
))

if res.role is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `role_id`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        | 123:owner                                                                  |
| `role_payload`                                                             | [Optional[components.RolePayload]](../../models/components/rolepayload.md) | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |


### Response

**[operations.PutRoleResponse](../../models/operations/putroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## refresh_permissions

Makes sure the user has a role in the organization

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.refresh_permissions()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.RefreshPermissionsResponse](../../models/operations/refreshpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## search_roles

Search Roles

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.roles.search_roles(request=components.RoleSearchInput(
    limit=1,
    offset=1,
    org_ids=[
        '123',
        '456',
    ],
    query='Administrator',
    role_ids=[
        '123:manager',
        '456:owner',
    ],
    slugs=[
        'manager',
        'owner',
    ],
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.RoleSearchInput](../../models/components/rolesearchinput.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.SearchRolesResponse](../../models/operations/searchrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
