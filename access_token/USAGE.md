<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_access_token
from epilot_access_token import Epilot

with Epilot(
    security=epilot_access_token.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.access_tokens.create_access_token(request={
        "name": "API Access Token",
        "assignments": [
            "123:owner",
        ],
        "token_type": epilot_access_token.TokenType.API,
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_access_token
from epilot_access_token import Epilot

async def main():
    async with Epilot(
        security=epilot_access_token.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:

        res = await epilot.access_tokens.create_access_token_async(request={
            "name": "API Access Token",
            "assignments": [
                "123:owner",
            ],
            "token_type": epilot_access_token.TokenType.API,
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->