<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_internal_auth import Epilot

with Epilot(
    sigv4="<YOUR_API_KEY_HERE>",
) as epilot:

    res = epilot.get_jwks()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_internal_auth import Epilot

async def main():
    async with Epilot(
        sigv4="<YOUR_API_KEY_HERE>",
    ) as epilot:

        res = await epilot.get_jwks_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->