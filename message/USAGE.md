<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_message
from epilot_message import Epilot

async def main():
    s = Epilot(
        security=epilot_message.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.drafts.create_draft_async(request=epilot_message.MessageRequestParams(
        from_={
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
        subject="Request for solar panel price",
        bcc=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
        cc=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
        file={
            "dollar_relation": [
                {
                    "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                    "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                    "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
                },
            ],
        },
        html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
        parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
        reply_to={
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
        text="We at ABC GmbH would like to request a price quote for the solar panel.",
        thread={
            "topic": "CUSTOMER_MESSAGE",
            "assigned_to": [
                "206801",
                "200109",
            ],
        },
        to=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
    ))
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->