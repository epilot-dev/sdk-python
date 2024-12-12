<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.group.advance_user_assignment(id="<id>")

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_user import Epilot

async def main():
    async with Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as epilot:

        res = await epilot.group.advance_user_assignment_async(id="<id>")

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->