<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->