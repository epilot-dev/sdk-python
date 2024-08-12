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
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.get_me()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.User](../../models/user.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_user

Get user by id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.get_user(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User id                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.User](../../models/user.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_user_login_parameters

Get user organization login parameters by username

### Example Usage

```python
from epilot_user import Epilot

s = Epilot()


res = s.user_v1.get_user_login_parameters(username="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Username                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetUserLoginParametersResponseBody](../../models/getuserloginparametersresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_users

Lists users in organizations you have access to

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.list_users()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Limit the results size                                              |
| `offset`                                                            | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Specify the offset                                                  |
| `org_ids`                                                           | List[*str*]                                                         | :heavy_minus_sign:                                                  | Comma-separated list of organization ids to filter by               |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Query text to filter by                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListUsersResponseBody](../../models/listusersresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
