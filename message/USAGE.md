<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->