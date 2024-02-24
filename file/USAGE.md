<!-- Start SDK Example Usage [usage] -->
```python
import epilot

s = epilot.Epilot()


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->