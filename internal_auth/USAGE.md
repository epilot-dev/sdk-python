<!-- Start SDK Example Usage -->


```python
import epilot

s = epilot.Epilot(
    sigv4="",
)


res = s.get_jwks()

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->