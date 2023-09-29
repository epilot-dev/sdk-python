# UserV1
(*user_v1*)

## Overview

Legacy User API

### Available Operations

* [get_me](#get_me) - getMe
* [get_user](#get_user) - getUser
* [get_user_login_parameters](#get_user_login_parameters) - getUserLoginParameters
* [list_users](#list_users) - listUsers

## get_me

Get currently logged in user

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
```


### Response

**[operations.GetMeResponse](../../models/operations/getmeresponse.md)**


## get_user

Get user by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetUserRequest(
    id='<ID>',
)

res = s.user_v1.get_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**


## get_user_login_parameters

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetUserLoginParametersRequest(
    username='Matilda.Jenkins64',
)

res = s.user_v1.get_user_login_parameters(req)

if res.get_user_login_parameters_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUserLoginParametersRequest](../../models/operations/getuserloginparametersrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUserLoginParametersResponse](../../models/operations/getuserloginparametersresponse.md)**


## list_users

Lists users in organizations you have access to

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ListUsersRequest(
    limit=5262.12,
    offset=5400.61,
    org_ids=[
        'Kentucky',
    ],
    query='West exploit versus',
)

res = s.user_v1.list_users(req)

if res.list_users_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListUsersRequest](../../models/operations/listusersrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**

