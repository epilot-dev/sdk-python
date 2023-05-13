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
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteRoleRequest(
    role_id='123:owner',
)

res = s.roles.delete_role(req)

if res.role is not None:
    # handle response
```

## get_role

Get role by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetRoleRequest(
    role_id='123:owner',
)

res = s.roles.get_role(req)

if res.role is not None:
    # handle response
```

## list_all_roles

Returns list of all roles in organization

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.roles.list_all_roles()

if res.list_all_roles_200_application_json_object is not None:
    # handle response
```

## list_current_roles

Returns roles and grants assigned to current user

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.roles.list_current_roles()

if res.list_current_roles_200_application_json_object is not None:
    # handle response
```

## put_role

Create or update role

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'nulla',
                            'corrupti',
                            'illum',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'error',
                            'deserunt',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'iure',
                            'magnam',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'ipsa',
                            'delectus',
                            'tempora',
                            'suscipit',
                        ],
                    ),
                ],
                effect=shared.GrantEffectEnum.ALLOW,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                conditions=[
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'voluptatum',
                            'iusto',
                            'excepturi',
                            'nisi',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'temporibus',
                            'ab',
                            'quis',
                            'veritatis',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'perferendis',
                            'ipsam',
                            'repellendus',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'quo',
                            'odit',
                            'at',
                            'at',
                        ],
                    ),
                ],
                effect=shared.GrantEffectEnum.DENY,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                conditions=[
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'quod',
                            'esse',
                            'totam',
                            'porro',
                        ],
                    ),
                    shared.EqualsCondition(
                        attribute='workflows.primary.task_name',
                        operation=shared.EqualsConditionOperationEnum.EQUALS,
                        values=[
                            'dicta',
                            'nam',
                            'officia',
                        ],
                    ),
                ],
                effect=shared.GrantEffectEnum.DENY,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
        ],
        id='123:owner',
        name='Owner',
        organization_id='123',
        slug='owner',
        type=operations.PutRoleRequestBody3TypeEnum.SHARE_ROLE,
    ),
    role_id='123:owner',
)

res = s.roles.put_role(req)

if res.role is not None:
    # handle response
```

## refresh_permissions

Makes sure the user has a role in the organization

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.roles.refresh_permissions()

if res.status_code == 200:
    # handle response
```

## search_roles

Search Roles

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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
