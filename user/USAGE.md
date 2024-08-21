<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.advance_user_assignment(id="<value>")

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
    s = Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.group.advance_user_assignment_async(id="<value>")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->