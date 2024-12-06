<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as s:
    res = s.file.delete_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8", activity_id="01F130Q52Q6MWSNS8N2AVXV4JN")

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_file
from epilot_file import Epilot

async def main():
    async with Epilot(
        security=epilot_file.Security(
            cookie_auth="<YOUR_API_KEY_HERE>",
        ),
    ) as s:
        res = await s.file.delete_file_async(id="ef7d985c-2385-44f4-9c71-ae06a52264f8", activity_id="01F130Q52Q6MWSNS8N2AVXV4JN")

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->