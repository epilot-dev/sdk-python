<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.JourneyTokenParameters(
    journey_id='provident',
    name='Postman Access Token',
    token_type=shared.JourneyTokenParametersTokenTypeEnum.JOURNEY,
)

res = s.access_tokens.create_access_token(req)

if res.create_access_token_201_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->