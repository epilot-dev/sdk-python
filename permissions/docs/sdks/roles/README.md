# roles

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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteRoleRequest(
    role_id='123:owner',
)

res = s.roles.delete_role(req)

if res.role is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteRoleRequest](../../models/operations/deleterolerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**


## get_role

Get role by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRoleRequest(
    role_id='123:owner',
)

res = s.roles.get_role(req)

if res.role is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetRoleRequest](../../models/operations/getrolerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**


## list_all_roles

Returns list of all roles in organization

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.roles.list_all_roles()

if res.list_all_roles_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListAllRolesResponse](../../models/operations/listallrolesresponse.md)**


## list_current_roles

Returns roles and grants assigned to current user

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.roles.list_current_roles()

if res.list_current_roles_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListCurrentRolesResponse](../../models/operations/listcurrentrolesresponse.md)**


## put_role

Create or update role

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PutRoleRequest(
    request_body=operations.PutRoleRequestBody3(
        expires_at=dateutil.parser.isoparse('2028-07-21T17:32:28Z'),
        grants=[
            shared.Grant(
                action='entity-read',
                conditions=[
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'nulla',
                            'corrupti',
                            'illum',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'error',
                            'deserunt',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'iure',
                            'magnam',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'ipsa',
                            'delectus',
                            'tempora',
                            'suscipit',
                        ],
                    ),
                ],
                effect=shared.GrantEffect.ALLOW,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                conditions=[
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'voluptatum',
                            'iusto',
                            'excepturi',
                            'nisi',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'temporibus',
                            'ab',
                            'quis',
                            'veritatis',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'perferendis',
                            'ipsam',
                            'repellendus',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'quo',
                            'odit',
                            'at',
                            'at',
                        ],
                    ),
                ],
                effect=shared.GrantEffect.DENY,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                conditions=[
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'quod',
                            'esse',
                            'totam',
                            'porro',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperation.EQUALS,
                        values=[
                            'dicta',
                            'nam',
                            'officia',
                        ],
                    ),
                ],
                effect=shared.GrantEffect.DENY,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
        ],
        id='123:owner',
        name='Owner',
        organization_id='123',
        slug='owner',
        type=operations.PutRoleRequestBody3Type.SHARE_ROLE,
    ),
    role_id='123:owner',
)

res = s.roles.put_role(req)

if res.role is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.PutRoleRequest](../../models/operations/putrolerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PutRoleResponse](../../models/operations/putroleresponse.md)**


## refresh_permissions

Makes sure the user has a role in the organization

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.roles.refresh_permissions()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.RefreshPermissionsResponse](../../models/operations/refreshpermissionsresponse.md)**


## search_roles

Search Roles

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.RoleSearchInput(
    limit=1,
    offset=1,
    org_ids=[
        '123',
    ],
    query='Administrator',
    role_ids=[
        '123:owner',
        '123:owner',
        '123:owner',
    ],
    slugs=[
        'owner',
        'owner',
        'owner',
        'owner',
    ],
)

res = s.roles.search_roles(req)

if res.search_roles_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.RoleSearchInput](../../models/shared/rolesearchinput.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.SearchRolesResponse](../../models/operations/searchrolesresponse.md)**

