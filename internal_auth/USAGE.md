<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

    
res = s.get_jwks()

if res.get_jwks_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->