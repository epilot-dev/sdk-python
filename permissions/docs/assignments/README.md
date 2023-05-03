# assignments

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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.AddAssignmentRequest(
    role_id='123:owner',
    user_id='1',
)

res = s.assignments.add_assignment(req)

if res.assignment is not None:
    # handle response
```

## assign_roles

Assign / unassign roles to users.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.AssignRolesRequest(
    request_body=[
        '123:owner',
        '123:owner',
        '123:owner',
    ],
    user_id='1',
)

res = s.assignments.assign_roles(req)

if res.assignments is not None:
    # handle response
```

## get_assigned_roles_for_user

Get list of assigned roles by user id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetAssignedRolesForUserRequest(
    user_id='1',
)

res = s.assignments.get_assigned_roles_for_user(req)

if res.assignments is not None:
    # handle response
```

## list_all_assignments

Returns list of all assignments in organization

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.assignments.list_all_assignments()

if res.list_all_assignments_200_application_json_object is not None:
    # handle response
```

## remove_assignment

Remove role assignment from user

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RemoveAssignmentRequest(
    role_id='123:owner',
    user_id='1',
)

res = s.assignments.remove_assignment(req)

if res.assignment is not None:
    # handle response
```
