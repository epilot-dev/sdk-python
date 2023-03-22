<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.JourneyTokenParameters(
    journey_id="deserunt",
    name="Postman Access Token",
    token_type="journey",
)
    
res = s.access_tokens.create_access_token(req)

if res.create_access_token_201_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->