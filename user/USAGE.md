<!-- Start SDK Example Usage -->
```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
```
<!-- End SDK Example Usage -->