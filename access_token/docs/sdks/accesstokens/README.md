# AccessTokens
(*access_tokens*)

## Overview

Create Access Tokens for epilot APIs

### Available Operations

* [create_access_token](#create_access_token) - createAccessToken
* [list_access_tokens](#list_access_tokens) - listAccessTokens
* [revoke_access_token](#revoke_access_token) - revokeAccessToken

## create_access_token

**Access Token type: `API`** (default if not specified):

Generates a new Access Token to use for calling epilot APIs.

Takes optionally a list of Roles assigned to the Access Token. Defaults to current user's assignments

See [Permissions API docs](https://docs.epilot.io/api/permissions)

**Access Token type: `JOURNEY`**:

Generates a Public Access Token related to a journey.
The journey id should be specfied.


### Example Usage

```python
import epilot_access_token
from epilot_access_token import Epilot

s = Epilot(
    security=epilot_access_token.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.access_tokens.create_access_token(request={
    "name": "Postman Access Token",
    "assignments": [
        "123:owner",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TokenParameters](../../models/tokenparameters.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CreateAccessTokenResponseBody](../../models/createaccesstokenresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_access_tokens

Lists all Access Tokens for current user (by default excludes system generated tokens)

### Example Usage

```python
import epilot_access_token
from epilot_access_token import Epilot

s = Epilot(
    security=epilot_access_token.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.access_tokens.list_access_tokens(token_type=[
    epilot_access_token.AccessTokenType.API,
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token_type`                                                        | List[[models.AccessTokenType](../../models/accesstokentype.md)]     | :heavy_minus_sign:                                                  | Filter by token types                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.AccessTokenItem]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## revoke_access_token

Revokes an Access Token so it can't be used anymore.

### Example Usage

```python
import epilot_access_token
from epilot_access_token import Epilot

s = Epilot(
    security=epilot_access_token.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.access_tokens.revoke_access_token(id="api_5ZugdRXasLfWBypHi93Fk")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | api_5ZugdRXasLfWBypHi93Fk                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AccessTokenItem](../../models/accesstokenitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
