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
    bcc=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
    cc=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
    file=components.AttachmentsRelation(
        dollar_relation=[
            components.File(
                cid='fb222496-a1a5-4639-94f2-07b5e35e4068',
                entity_id='f820ce3b-07b0-45ae-bcc6-babb2f53f79f',
                filename='Produktinformationen_epilot360_Double_Opt_in.pdf',
            ),
        ],
    ),
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error=components.SendError(),
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error=components.SendError(),
    ),
    subject='Request for solar panel price',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        assigned_to=[
            'string',
        ],
        topic='string',
    ),
    to=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->