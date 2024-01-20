<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->