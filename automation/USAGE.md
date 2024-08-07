<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executions.cancel_execution(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_automation import Epilot

async def main():
    s = Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.executions.cancel_execution_async(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->