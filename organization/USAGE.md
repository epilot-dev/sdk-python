<!-- Start SDK Example Usage [usage] -->
```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization.get_organization(org_id='739224')

if res.organization is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->