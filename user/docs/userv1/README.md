# user_v1

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


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
```

## get_user

Get user by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetUserRequest(
    id="89bd9d8d-69a6-474e-8f46-7cc8796ed151",
)

res = s.user_v1.get_user(req)

if res.user is not None:
    # handle response
```

## get_user_login_parameters

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetUserLoginParametersRequest(
    username="Lydia_Aufderhar",
)

res = s.user_v1.get_user_login_parameters(req)

if res.get_user_login_parameters_200_application_json_object is not None:
    # handle response
```

## list_users

Lists users in organizations you have access to

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListUsersRequest(
    limit=9571.56,
    offset=7781.57,
    org_ids=[
        "at",
    ],
    query="at",
)

res = s.user_v1.list_users(req)

if res.list_users_200_application_json_object is not None:
    # handle response
```
