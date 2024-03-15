<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot()


res = s.ecp_admin.can_trigger_portal_flow("<YOUR_BEARER_TOKEN_HERE>", trigger_portal_flow=components.TriggerPortalFlow(
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->