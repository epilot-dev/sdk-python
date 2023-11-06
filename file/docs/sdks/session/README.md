# Session
(*session*)

## Overview

Session API for cookie authentication

### Available Operations

* [delete_session](#delete_session) - deleteSession
* [get_session](#get_session) - getSession

## delete_session

End browser session by deleting token cookie

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)


res = s.session.delete_session()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.DeleteSessionResponse](../../models/operations/deletesessionresponse.md)**


## get_session

Start a browser session by setting passed Authorization token in a server side cookie.

Allows using preview urls directly in img src for private files using cookie authentication.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)


res = s.session.get_session()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**

