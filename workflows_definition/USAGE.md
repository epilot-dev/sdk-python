<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.closing_reason.change_reason_status(reason_id="<value>")

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from openapi import SDK

async def main():
    s = SDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    await s.closing_reason.change_reason_status_async(reason_id="<value>")
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->