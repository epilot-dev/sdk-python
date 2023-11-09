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
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = s.access_tokens.create_access_token(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [Union[shared.AccessTokenParameters, shared.JourneyTokenParameters]](../../models/shared/tokenparameters.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreateAccessTokenResponse](../../models/operations/createaccesstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_access_tokens

Lists all Access Tokens for current user (by default excludes system generated tokens)

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.access_tokens.list_access_tokens(token_type=[
    shared.AccessTokenType.API,
])

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `token_type`                                                           | List[[shared.AccessTokenType](../../models/shared/accesstokentype.md)] | :heavy_minus_sign:                                                     | Filter by token types                                                  |


### Response

**[operations.ListAccessTokensResponse](../../models/operations/listaccesstokensresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## revoke_access_token

Revokes an Access Token so it can't be used anymore.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.access_tokens.revoke_access_token(id='api_5ZugdRXasLfWBypHi93Fk')

if res.access_token_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                 | Type                      | Required                  | Description               | Example                   |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `id`                      | *str*                     | :heavy_check_mark:        | N/A                       | api_5ZugdRXasLfWBypHi93Fk |


### Response

**[operations.RevokeAccessTokenResponse](../../models/operations/revokeaccesstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
