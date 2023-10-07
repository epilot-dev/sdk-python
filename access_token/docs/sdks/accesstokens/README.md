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

req = {
    "SAS": 'Nissan',
}

res = s.access_tokens.create_access_token(req)

if res.create_access_token_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateAccessTokenResponse](../../models/operations/createaccesstokenresponse.md)**


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

req = operations.ListAccessTokensRequest(
    token_type=[
        shared.AccessTokenType.API,
    ],
)

res = s.access_tokens.list_access_tokens(req)

if res.access_token_items is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAccessTokensRequest](../../models/operations/listaccesstokensrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListAccessTokensResponse](../../models/operations/listaccesstokensresponse.md)**


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

req = operations.RevokeAccessTokenRequest(
    id='api_5ZugdRXasLfWBypHi93Fk',
)

res = s.access_tokens.revoke_access_token(req)

if res.access_token_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RevokeAccessTokenRequest](../../models/operations/revokeaccesstokenrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RevokeAccessTokenResponse](../../models/operations/revokeaccesstokenresponse.md)**

