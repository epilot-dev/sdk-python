<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_permissions
from epilot_permissions import Epilot

s = Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.add_assignment(role_id="123:owner", user_id="1")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_permissions
from epilot_permissions import Epilot

async def main():
    s = Epilot(
        security=epilot_permissions.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.assignments.add_assignment_async(role_id="123:owner", user_id="1")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->