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
    epilot_auth="",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass
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
    epilot_auth="",
)


res = s.user_v1.get_user(id='string')

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | User id            |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**


## get_user_login_parameters

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v1.get_user_login_parameters(username='string')

if res.get_user_login_parameters_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `username`         | *str*              | :heavy_check_mark: | Username           |


### Response

**[operations.GetUserLoginParametersResponse](../../models/operations/getuserloginparametersresponse.md)**


## list_users

Lists users in organizations you have access to

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v1.list_users(limit=5262.12, offset=5400.61, org_ids=[
    'string',
], query='string')

if res.list_users_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `limit`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | Limit the results size                                |
| `offset`                                              | *Optional[float]*                                     | :heavy_minus_sign:                                    | Specify the page                                      |
| `org_ids`                                             | List[*str*]                                           | :heavy_minus_sign:                                    | Comma-separated list of organization ids to filter by |
| `query`                                               | *Optional[str]*                                       | :heavy_minus_sign:                                    | Query text to filter by                               |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**

