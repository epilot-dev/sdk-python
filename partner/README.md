# epilot-partner

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=partner
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot()


res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [partners](docs/sdks/partners/README.md)

* [activate_partner](docs/sdks/partners/README.md#activate_partner) - activatePartner
* [approve_partner](docs/sdks/partners/README.md#approve_partner) - approvePartner
* [batch_get_assignable](docs/sdks/partners/README.md#batch_get_assignable) - batchGet
* [get_partner_by_token](docs/sdks/partners/README.md#get_partner_by_token) - getPartnerByToken
* [~~invite_partner~~](docs/sdks/partners/README.md#invite_partner) - invitePartner :warning: **Deprecated**
* [invite_partner_v2](docs/sdks/partners/README.md#invite_partner_v2) - invitePartnerV2
* [reject_partner](docs/sdks/partners/README.md#reject_partner) - rejectPartner
* [~~resend_partner_invitation~~](docs/sdks/partners/README.md#resend_partner_invitation) - resendPartnerInvitation :warning: **Deprecated**
* [search_assignable](docs/sdks/partners/README.md#search_assignable) - searchAssignables
* [search_geolocation_for_text](docs/sdks/partners/README.md#search_geolocation_for_text) - searchGeolocationForText
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import epilot
from epilot.models import errors, shared

s = epilot.Epilot()


res = None
try:
    res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))
except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://partner-directory-api.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_idx=0,
)


res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_url="https://partner-directory-api.sls.epilot.io",
)


res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name              | Type              | Scheme            |
| ----------------- | ----------------- | ----------------- |
| `as_organization` | apiKey            | API key           |
| `epilot_auth`     | http              | HTTP Bearer       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
