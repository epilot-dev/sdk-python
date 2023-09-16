# Assignments

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
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
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

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.AddAssignmentRequest](../../models/operations/addassignmentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.AddAssignmentResponse](../../models/operations/addassignmentresponse.md)**


## assign_roles

Assign / unassign roles to users.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AssignRolesRequest(
    request_body=[
        '123:owner',
    ],
    user_id='1',
)

res = s.assignments.assign_roles(req)

if res.assignments is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AssignRolesRequest](../../models/operations/assignrolesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.AssignRolesResponse](../../models/operations/assignrolesresponse.md)**


## get_assigned_roles_for_user

Get list of assigned roles by user id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetAssignedRolesForUserRequest(
    user_id='1',
)

res = s.assignments.get_assigned_roles_for_user(req)

if res.assignments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAssignedRolesForUserRequest](../../models/operations/getassignedrolesforuserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetAssignedRolesForUserResponse](../../models/operations/getassignedrolesforuserresponse.md)**


## list_all_assignments

Returns list of all assignments in organization

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.assignments.list_all_assignments()

if res.list_all_assignments_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListAllAssignmentsResponse](../../models/operations/listallassignmentsresponse.md)**


## remove_assignment

Remove role assignment from user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
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

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveAssignmentRequest](../../models/operations/removeassignmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveAssignmentResponse](../../models/operations/removeassignmentresponse.md)**

