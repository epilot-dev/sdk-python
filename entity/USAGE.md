<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.activity.attach_activity(request={
        "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_entity
from epilot_entity import Epilot

async def main():
    async with Epilot(
        security=epilot_entity.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:
        res = await epilot.activity.attach_activity_async(request={
            "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->