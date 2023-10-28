<!-- Start SDK Example Usage -->


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

if res.create_access_token_201_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->