<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.can_trigger_portal_flow(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, trigger_portal_flow={
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
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
import epilot_customer_portal
from epilot_customer_portal import Epilot

async def main():
    s = Epilot(
        security=epilot_customer_portal.Security(
            either_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.ecp_admin.can_trigger_portal_flow_async(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, trigger_portal_flow={
        "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->