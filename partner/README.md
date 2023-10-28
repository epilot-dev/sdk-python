# epilot-partner

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=partner
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)

req = operations.ActivatePartnerRequest(
    activate_partner_payload=shared.ActivatePartnerPayload(
        company_name='Company name',
        organization_id='string',
        signed_up_email='Lupe.Graham2@hotmail.com',
    ),
    token='string',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [partners](docs/sdks/partners/README.md)

* [activate_partner](docs/sdks/partners/README.md#activate_partner) - activatePartner
* [approve_partner](docs/sdks/partners/README.md#approve_partner) - approvePartner
* [batch_get_assignable](docs/sdks/partners/README.md#batch_get_assignable) - batchGet
* [get_partner_by_token](docs/sdks/partners/README.md#get_partner_by_token) - getPartnerByToken
* [invite_partner](docs/sdks/partners/README.md#invite_partner) - invitePartner
* [reject_partner](docs/sdks/partners/README.md#reject_partner) - rejectPartner
* [resend_partner_invitation](docs/sdks/partners/README.md#resend_partner_invitation) - resendPartnerInvitation
* [search_assignable](docs/sdks/partners/README.md#search_assignable) - searchAssignables
* [search_geolocation_for_text](docs/sdks/partners/README.md#search_geolocation_for_text) - searchGeolocationForText
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://partner-directory-api.sls.epilot.io` | None |

For example:


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
    server_idx=0
)

req = operations.ActivatePartnerRequest(
    activate_partner_payload=shared.ActivatePartnerPayload(
        company_name='Company name',
        organization_id='string',
        signed_up_email='Lupe.Graham2@hotmail.com',
    ),
    token='string',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
    server_url="https://partner-directory-api.sls.epilot.io"
)

req = operations.ActivatePartnerRequest(
    activate_partner_payload=shared.ActivatePartnerPayload(
        company_name='Company name',
        organization_id='string',
        signed_up_email='Lupe.Graham2@hotmail.com',
    ),
    token='string',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
