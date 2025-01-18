<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.executions.cancel_execution(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_automation import Epilot

async def main():
    async with Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as epilot:

        res = await epilot.executions.cancel_execution_async(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->