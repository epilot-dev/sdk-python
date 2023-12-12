<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
<!-- End SDK Example Usage [usage] -->