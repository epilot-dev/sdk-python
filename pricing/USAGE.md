<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    currency='EUR',
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->