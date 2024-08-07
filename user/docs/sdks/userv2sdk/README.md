# UserV2SDK
(*user_v2*)

## Overview

User API V2

### Available Operations

* [activate_user](#activate_user) - activateUser
* [delete_user_v2](#delete_user_v2) - deleteUserV2
* [get_me_v2](#get_me_v2) - getMeV2
* [get_user_login_parameters_v2](#get_user_login_parameters_v2) - getUserLoginParametersV2
* [get_user_v2](#get_user_v2) - getUserV2
* [invite_user](#invite_user) - inviteUser
* [list_users_v2](#list_users_v2) - listUsersV2
* [resend_user_invitation](#resend_user_invitation) - resendUserInvitation
* [sign_up_user](#sign_up_user) - signUpUser
* [update_user_v2](#update_user_v2) - updateUserV2
* [verify_email_with_token](#verify_email_with_token) - verifyEmailWithToken

## activate_user

Activate user using an invite token

### Example Usage

```python
from epilot_user import Epilot

s = Epilot()


s.user_v2.activate_user(token="<value>", user_activation_payload={
    "display_name": "Example User",
    "password": "AKjhdakjsdh@!34",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `token`                                                                         | *str*                                                                           | :heavy_check_mark:                                                              | Invite Token                                                                    |
| `user_activation_payload`                                                       | [Optional[models.UserActivationPayload]](../../models/useractivationpayload.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_user_v2

Delete user by user id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.delete_user_v2(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.User](../../models/user.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_me_v2

Get currently logged in user

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.get_me_v2()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UserV2](../../models/userv2.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_user_login_parameters_v2

Get user organization login parameters by username

### Example Usage

```python
from epilot_user import Epilot

s = Epilot()


res = s.user_v2.get_user_login_parameters_v2(username="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Username                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetUserLoginParametersV2ResponseBody](../../models/getuserloginparametersv2responsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_user_v2

Get user details by user id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.get_user_v2(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UserV2](../../models/userv2.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## invite_user

Creates a new user in the caller's organization and sends an invite email to activate

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.invite_user(request={
    "email": "test@example.com",
    "roles": [
        "123:owner",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UserInvitationPayload](../../models/userinvitationpayload.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.UserV2](../../models/userv2.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_users_v2

Get the list of organization users

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.list_users_v2()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Limit the results size                                              |
| `offset`                                                            | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Specify the offset                                                  |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Query text to filter by                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListUsersV2ResponseBody](../../models/listusersv2responsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## resend_user_invitation

Resend user invitation email

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.resend_user_invitation(request={
    "email": "test@example.com",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.ResendUserInvitationRequestBody](../../models/resenduserinvitationrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |


### Response

**[models.UserV2](../../models/userv2.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## sign_up_user

signUpUser

### Example Usage

```python
import epilot_user
from epilot_user import Epilot

s = Epilot()


res = s.user_v2.sign_up_user(signup_user_payload={
    "organization_detail": epilot_user.OrganizationDetail(
        email="Jettie71@yahoo.com",
        name="Epilot",
        pricing_tier="professional",
        type=epilot_user.OrganizationDetailType.PARTNER,
        is_privacy_policy_checked=False,
        is_terms_and_conditions_checked=False,
    ),
    "user_detail": {
        "email": "Caden82@hotmail.com",
        "full_name": "Example user",
        "password": "AKjhdakjsdh@!34",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `token`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Invitation partner token                                                |
| `signup_user_payload`                                                   | [Optional[models.SignupUserPayload]](../../models/signupuserpayload.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |


### Response

**[models.SignUpUserResponseBody](../../models/signupuserresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_user_v2

Update user details

### Example Usage

```python
import epilot_user
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_v2.update_user_v2(id="<value>", user_v2={
    "created_at": "2022-02-08T04:44:32.246Z",
    "department": "Sales",
    "display_name": "Example User",
    "favorites": {
        "entity_views": {
            "opportunity": "891a5409850abf8b92bd2cb7bdd2844d32ce6bec",
            "order": "628aee91-7c2f-4047-ab0d-433582a19c49",
        },
        "dashboard": "751ff121-9ac2-4511-a2e6-851f11287380",
    },
    "feature_preferences": {
        "feature_name": True,
    },
    "image_uri": epilot_user.UserV2ImageURI(
        original="https://account-profile-images.epilot.cloud/1/avatar.png",
        thumbnail_32="https://account-profile-images.epilot.cloud/1/avatar_32x32.png",
        **{

        },
    ),
    "is_signature_enabled": True,
    "mfa_enabled": False,
    "phone": "1234567890",
    "phone_verified": True,
    "preferred_language": "de",
    "properties": [
        {
            "name": "profileImageName",
            "value": "avatar.png",
        },
    ],
    "secondary_phone": "1234567890",
    "signature": "<p>Thanks</p>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `user_v2`                                                           | [Optional[models.UserV2Input]](../../models/userv2input.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UserV2](../../models/userv2.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## verify_email_with_token

Update new email using an verification token

### Example Usage

```python
from epilot_user import Epilot

s = Epilot()


s.user_v2.verify_email_with_token(token="<value>", user_verification_payload={
    "password": "AKjhdakjsdh@!34",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `token`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | Verification Token                                                                  |
| `user_verification_payload`                                                         | [Optional[models.UserVerificationPayload]](../../models/userverificationpayload.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
