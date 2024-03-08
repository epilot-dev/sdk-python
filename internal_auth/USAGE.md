<!-- Start SDK Example Usage [usage] -->
```python
import epilot

s = epilot.Epilot(
    sigv4="<YOUR_API_KEY_HERE>",
)


res = s.get_jwks()

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->