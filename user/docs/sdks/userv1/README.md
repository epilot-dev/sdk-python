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

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass
```


### Response

**[operations.GetMeResponse](../../models/operations/getmeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user

Get user by id

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.get_user(id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user_login_parameters

Get user organization login parameters by username

### Example Usage

```python
import epilot

s = epilot.Epilot()


res = s.user_v1.get_user_login_parameters(username='<value>')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `username`         | *str*              | :heavy_check_mark: | Username           |


### Response

**[operations.GetUserLoginParametersResponse](../../models/operations/getuserloginparametersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_users

Lists users in organizations you have access to

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.list_users(limit=5262.12, offset=5400.61, org_ids=[
    '<value>',
], query='<value>')

if res.object is not None:
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
