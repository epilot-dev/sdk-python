<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = "unde"
    
res = s.drafts.create_draft(req)

if res.create_draft_201_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->