<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_partner import Epilot

s = Epilot()


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
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
    s = Epilot()
    await s.partners.activate_partner_async(token="<value>", activate_partner_payload={
        "organization_id": "<value>",
        "signed_up_email": "Flavio.Ankunding@hotmail.com",
        "company_name": "Company name",
    })
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->