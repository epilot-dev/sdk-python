<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.can_trigger_portal_flow(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, activity_id="01F130Q52Q6MWSNS8N2AVXV4JN", ecp_config={
        "file_config": {
            "tags": [
                "example",
                "mock",
            ],
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_customer_portal
from epilot_customer_portal import Epilot

async def main():
    async with Epilot(
        security=epilot_customer_portal.Security(
            either_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:

        res = await epilot.ecp_admin.can_trigger_portal_flow_async(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, activity_id="01F130Q52Q6MWSNS8N2AVXV4JN", ecp_config={
            "file_config": {
                "tags": [
                    "example",
                    "mock",
                ],
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->