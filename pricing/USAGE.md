<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
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
import dateutil.parser
from epilot_pricing import Epilot

async def main():
    s = Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.catalog_api.dollar_private_search_catalog_async(request={
        "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
        "availability": {
            "location": {},
            "available_date": dateutil.parser.parse("2017-07-21").date(),
        },
        "from_": 0,
        "size": 200,
        "sort": "description ASC",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->