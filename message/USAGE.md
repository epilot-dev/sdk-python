<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.MessageRequestParams(
    bcc=[
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "distinctio": "quibusdam",
                "unde": "nulla",
                "corrupti": "illum",
            },
            send_status="REJECT",
        ),
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "deserunt": "suscipit",
                "iure": "magnam",
                "debitis": "ipsa",
            },
            send_status="ERROR",
        ),
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "suscipit": "molestiae",
                "minus": "placeat",
            },
            send_status="COMPLAINT",
        ),
    ],
    cc=[
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "nisi": "recusandae",
                "temporibus": "ab",
                "quis": "veritatis",
            },
            send_status="COMPLAINT",
        ),
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "ipsam": "repellendus",
            },
            send_status="ERROR",
        ),
    ],
    file=shared.AttachmentsRelation(
        dollar_relation=[
            shared.File(
                cid="fb222496-a1a5-4639-94f2-07b5e35e4068",
                entity_id="f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                filename="Produktinformationen_epilot360_Double_Opt_in.pdf",
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
            shared.File(
                cid="fb222496-a1a5-4639-94f2-07b5e35e4068",
                entity_id="f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                filename="Produktinformationen_epilot360_Double_Opt_in.pdf",
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
            shared.File(
                cid="fb222496-a1a5-4639-94f2-07b5e35e4068",
                entity_id="f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                filename="Produktinformationen_epilot360_Double_Opt_in.pdf",
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
            shared.File(
                cid="fb222496-a1a5-4639-94f2-07b5e35e4068",
                entity_id="f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                filename="Produktinformationen_epilot360_Double_Opt_in.pdf",
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
        ],
    ),
    from_=shared.Address(
        address="messaging@epilot.cloud",
        name="epilot",
        send_error={
            "at": "at",
        },
        send_status="ERROR",
    ),
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to=shared.Address(
        address="messaging@epilot.cloud",
        name="epilot",
        send_error={
            "quod": "quod",
            "esse": "totam",
        },
        send_status="BOUNCE",
    ),
    subject="Request for solar panel price",
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread=shared.MessageRequestParamsThread(
        assigned_to=[
            "dicta",
            "nam",
            "officia",
        ],
        topic="occaecati",
    ),
    to=[
        shared.Address(
            address="messaging@epilot.cloud",
            name="epilot",
            send_error={
                "hic": "optio",
                "totam": "beatae",
                "commodi": "molestiae",
            },
            send_status="DELIVERY",
        ),
    ],
)
    
res = s.drafts.create_draft(req)

if res.create_draft_201_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->