<!-- Start SDK Example Usage -->


```python
import epilot

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->