<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.deprecated.save_file(request=epilot_file.SaveS3FilePayload(
    id="ef7d985c-2385-44f4-9c71-ae06a52264f8",
    tags=[
        "tag1",
        "tag2",
    ],
    custom_download_url="https://some-api-url.com/download?file_id=123",
    filename="document.pdf",
    mime_type="application/pdf",
    relations=[
        {
            "entity_id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
            "schema_": "contact",
        },
    ],
    s3ref={
        "bucket": "epilot-prod-user-content",
        "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    },
))

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
    s = Epilot(
        security=epilot_file.Security(
            cookie_auth="<YOUR_API_KEY_HERE>",
        ),
    )
    res = await s.deprecated.save_file_async(request=epilot_file.SaveCustomFilePayload(
        id="ef7d985c-2385-44f4-9c71-ae06a52264f8",
        tags=[
            "tag1",
            "tag2",
        ],
        custom_download_url="https://some-api-url.com/download?file_id=123",
        filename="document.pdf",
        mime_type="application/pdf",
        relations=[
            {
                "entity_id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
                "schema_": "contact",
            },
        ],
    ))
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->