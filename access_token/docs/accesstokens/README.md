# access_tokens

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
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.JourneyTokenParameters(
    journey_id='quibusdam',
    name='Postman Access Token',
    token_type=shared.JourneyTokenParametersTokenTypeEnum.JOURNEY,
)

res = s.access_tokens.create_access_token(req)

if res.create_access_token_201_application_json_object is not None:
    # handle response
```

## list_access_tokens

Lists all Access Tokens for current user (by default excludes system generated tokens)

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListAccessTokensRequest(
    token_type=[
        shared.AccessTokenTypeEnum.API,
        shared.AccessTokenTypeEnum.API,
        shared.AccessTokenTypeEnum.API,
    ],
)

res = s.access_tokens.list_access_tokens(req)

if res.access_token_items is not None:
    # handle response
```

## revoke_access_token

Revokes an Access Token so it can't be used anymore.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RevokeAccessTokenRequest(
    id='api_5ZugdRXasLfWBypHi93Fk',
)

res = s.access_tokens.revoke_access_token(req)

if res.access_token_item is not None:
    # handle response
```
