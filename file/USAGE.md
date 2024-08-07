<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from epilot_file import Epilot

s = Epilot()


s.files.access_public_link(filename="invoice-2023-12.pdf", id="13d22918-36bd-4227-9ad4-2cb978788c8d")

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_file import Epilot

async def main():
    s = Epilot()
    await s.files.access_public_link_async(filename="invoice-2023-12.pdf", id="13d22918-36bd-4227-9ad4-2cb978788c8d")
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->