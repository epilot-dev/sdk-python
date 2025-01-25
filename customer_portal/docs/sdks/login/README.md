# Login
(*login*)

## Overview

### Available Operations

* [sso_login](#sso_login) - ssoLogin

## sso_login

Initiate login using external SSO identity.

Verifies the user with the issuer and matches the identity to an epilot user (or creates a new user).

Returns parameters to be used with CUSTOM_AUTH flow against Cognito


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot() as epilot:

    res = epilot.login.sso_login(security=epilot_customer_portal.SsoLoginSecurity(
        external_oidc_auth="<YOUR_BEARER_TOKEN_HERE>",
    ), org_id="123", origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, contact_id="5da0a718-c822-403d-9f5d-20d4584e0528", provider_slug="office-365-login")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.SsoLoginSecurity](../../models/ssologinsecurity.md)             | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `org_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | epilot organization id                                                  | 123                                                                     |
| `origin`                                                                | [models.Origin](../../models/origin.md)                                 | :heavy_check_mark:                                                      | Origin of the Portal                                                    |                                                                         |
| `contact_id`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | contact id in the epilot system                                         | 5da0a718-c822-403d-9f5d-20d4584e0528                                    |
| `provider_slug`                                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | URL-friendly slug to use as organization-unique identifier for Provider | office-365-login                                                        |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.SsoLoginResponseBody](../../models/ssologinresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |