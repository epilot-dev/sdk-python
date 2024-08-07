<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_access_token
from epilot_access_token import Epilot

s = Epilot(
    security=epilot_access_token.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.access_tokens.create_access_token(request={
    "name": "Postman Access Token",
    "assignments": [
        "123:owner",
    ],
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
import epilot_access_token
from epilot_access_token import Epilot

async def main():
    s = Epilot(
        security=epilot_access_token.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.access_tokens.create_access_token_async(request={
        "name": "Postman Access Token",
        "assignments": [
            "123:owner",
        ],
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->