# Assignments
(*assignments*)

## Overview

Assign roles to users

### Available Operations

* [add_assignment](#add_assignment) - addAssignment
* [assign_roles](#assign_roles) - assignRoles
* [get_assigned_roles_for_user](#get_assigned_roles_for_user) - getAssignedRolesForUser
* [list_all_assignments](#list_all_assignments) - listAllAssignments
* [remove_assignment](#remove_assignment) - removeAssignment

## add_assignment

Assign a user to a role.

Use the `x-epilot-org-id` header to assign share roles to users in other orgs


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.add_assignment(role_id='123:owner', user_id='1')

if res.assignment is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `role_id`          | *str*              | :heavy_check_mark: | N/A                | 123:owner          |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | 1                  |


### Response

**[operations.AddAssignmentResponse](../../models/operations/addassignmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## assign_roles

Assign / unassign roles to users.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.assign_roles(user_id='1', request_body=[
    '123:owner',
])

if res.assignments is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | 1                  |
| `request_body`     | List[*str*]        | :heavy_minus_sign: | N/A                |                    |


### Response

**[operations.AssignRolesResponse](../../models/operations/assignrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_assigned_roles_for_user

Get list of assigned roles by user id

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.get_assigned_roles_for_user(user_id='1')

if res.assignments is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | 1                  |


### Response

**[operations.GetAssignedRolesForUserResponse](../../models/operations/getassignedrolesforuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_all_assignments

Returns list of all assignments in organization

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.list_all_assignments()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ListAllAssignmentsResponse](../../models/operations/listallassignmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## remove_assignment

Remove role assignment from user

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.remove_assignment(role_id='123:owner', user_id='1')

if res.assignment is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `role_id`          | *str*              | :heavy_check_mark: | N/A                | 123:owner          |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | 1                  |


### Response

**[operations.RemoveAssignmentResponse](../../models/operations/removeassignmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
