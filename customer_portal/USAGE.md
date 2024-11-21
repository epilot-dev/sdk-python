<!-- Start SDK Example Usage -->


```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetEntityActivityFeedRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    slug=shared.EntitySlug.CONTACT,
    type='SyncActivity',
)

res = s.activity.get_entity_activity_feed(req)

if res.get_entity_activity_feed_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->