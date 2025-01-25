<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_permissions
from epilot_permissions import Epilot

with Epilot(
    security=epilot_permissions.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.assignments.add_assignment(role_id="123:owner", user_id="1")

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_permissions
from epilot_permissions import Epilot

async def main():
    async with Epilot(
        security=epilot_permissions.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:

        res = await epilot.assignments.add_assignment_async(role_id="123:owner", user_id="1")

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->