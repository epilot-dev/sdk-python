# epilot-user

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=user
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [user_v1](docs/sdks/userv1/README.md)

* [get_me](docs/sdks/userv1/README.md#get_me) - getMe
* [get_user](docs/sdks/userv1/README.md#get_user) - getUser
* [get_user_login_parameters](docs/sdks/userv1/README.md#get_user_login_parameters) - getUserLoginParameters
* [list_users](docs/sdks/userv1/README.md#list_users) - listUsers

### [user_v2](docs/sdks/userv2/README.md)

* [activate_user](docs/sdks/userv2/README.md#activate_user) - activateUser
* [delete_user_v2](docs/sdks/userv2/README.md#delete_user_v2) - deleteUserV2
* [get_me_v2](docs/sdks/userv2/README.md#get_me_v2) - getMeV2
* [get_user_login_parameters_v2](docs/sdks/userv2/README.md#get_user_login_parameters_v2) - getUserLoginParametersV2
* [get_user_v2](docs/sdks/userv2/README.md#get_user_v2) - getUserV2
* [invite_user](docs/sdks/userv2/README.md#invite_user) - inviteUser
* [list_users_v2](docs/sdks/userv2/README.md#list_users_v2) - listUsersV2
* [resend_user_invitation](docs/sdks/userv2/README.md#resend_user_invitation) - resendUserInvitation
* [sign_up_user](docs/sdks/userv2/README.md#sign_up_user) - signUpUser
* [update_user_v2](docs/sdks/userv2/README.md#update_user_v2) - updateUserV2
* [verify_email_with_token](docs/sdks/userv2/README.md#verify_email_with_token) - verifyEmailWithToken
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import epilot

s = epilot.Epilot(
    epilot_auth="",
)


res = None
try:
    res = s.user_v1.get_me()

except (errors.SDKError) as e:
    print(e) # handle exception


if res.user is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://user.sls.epilot.io` | None |

#### Example

```python
import epilot

s = epilot.Epilot(
    server_idx=0,
    epilot_auth="",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot

s = epilot.Epilot(
    server_url="https://user.sls.epilot.io",
    epilot_auth="",
)


res = s.user_v1.get_me()

if res.user is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |

To authenticate with the API the `epilot_auth` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
