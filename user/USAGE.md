<!-- Start SDK Example Usage [usage] -->
```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->