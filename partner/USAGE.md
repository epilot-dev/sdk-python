<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_partner import Epilot

with Epilot() as epilot:
    epilot.partners.activate_partner(token="<value>", activate_partner_payload={
        "organization_id": "<id>",
        "signed_up_email": "Ebony1@hotmail.com",
        "company_name": "Company name",
    })

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_partner import Epilot

async def main():
    async with Epilot() as epilot:
        await epilot.partners.activate_partner_async(token="<value>", activate_partner_payload={
            "organization_id": "<id>",
            "signed_up_email": "Ebony1@hotmail.com",
            "company_name": "Company name",
        })

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->