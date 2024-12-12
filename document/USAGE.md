<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_document
from epilot_document import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.documents.convert_document(request={
        "input_document": {
            "s3ref": {
                "bucket": "document-api-prod",
                "key": "uploads/my-template.pdf",
            },
        },
        "output_format": epilot_document.OutputFormat.PDF,
        "output_filename": "converted.pdf",
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
import epilot_document
from epilot_document import Epilot

async def main():
    async with Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as epilot:

        res = await epilot.documents.convert_document_async(request={
            "input_document": {
                "s3ref": {
                    "bucket": "document-api-prod",
                    "key": "uploads/my-template.pdf",
                },
            },
            "output_format": epilot_document.OutputFormat.PDF,
            "output_filename": "converted.pdf",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->