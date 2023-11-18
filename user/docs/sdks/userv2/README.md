# UserV2
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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.activate_user(token='string', user_activation_payload=shared.UserActivationPayload(
    display_name='Example User',
    password='AKjhdakjsdh@!34',
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `token`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | Invite Token                                                                           |
| `user_activation_payload`                                                              | [Optional[shared.UserActivationPayload]](../../models/shared/useractivationpayload.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.ActivateUserResponse](../../models/operations/activateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_user_v2

Delete user by user id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.delete_user_v2(id='string')

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | The Id of user     |


### Response

**[operations.DeleteUserV2Response](../../models/operations/deleteuserv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_me_v2

Get currently logged in user

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.get_me_v2()

if res.user_v2 is not None:
    # handle response
    pass
```


### Response

**[operations.GetMeV2Response](../../models/operations/getmev2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_user_login_parameters_v2

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.get_user_login_parameters_v2(username='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `username`         | *str*              | :heavy_check_mark: | Username           |


### Response

**[operations.GetUserLoginParametersV2Response](../../models/operations/getuserloginparametersv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_user_v2

Get user details by user id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.get_user_v2(id='string')

if res.user_v2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | The Id of user     |


### Response

**[operations.GetUserV2Response](../../models/operations/getuserv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## invite_user

Creates a new user in the caller's organization and sends an invite email to activate

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="",
)

req = shared.UserInvitationPayload(
    email='test@example.com',
    roles=[
        '1',
        '2',
        '3',
        ':',
        'o',
        'w',
        'n',
        'e',
        'r',
    ],
)

res = s.user_v2.invite_user(req)

if res.user_v2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.UserInvitationPayload](../../models/shared/userinvitationpayload.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.InviteUserResponse](../../models/operations/inviteuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_users_v2

Get the list of organization users

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.list_users_v2(limit=4589.67, offset=7253.59, query='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `limit`                 | *Optional[float]*       | :heavy_minus_sign:      | Limit the results size  |
| `offset`                | *Optional[float]*       | :heavy_minus_sign:      | Specify the page        |
| `query`                 | *Optional[str]*         | :heavy_minus_sign:      | Query text to filter by |


### Response

**[operations.ListUsersV2Response](../../models/operations/listusersv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## resend_user_invitation

Resend user invitation email

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)

req = operations.ResendUserInvitationRequestBody(
    email='test@example.com',
)

res = s.user_v2.resend_user_invitation(req)

if res.user_v2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ResendUserInvitationRequestBody](../../models/operations/resenduserinvitationrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ResendUserInvitationResponse](../../models/operations/resenduserinvitationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## sign_up_user

signUpUser

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.sign_up_user(signup_user_payload=shared.SignupUserPayload(
    organization_detail=shared.OrganizationDetail(
        additional_properties={
            "key": 'string',
        },
        email='Jettie71@yahoo.com',
        is_privacy_policy_checked=False,
        is_terms_and_conditions_checked=False,
        name='Epilot',
        pricing_tier='professional',
        type=shared.OrganizationDetailType.PARTNER,
    ),
    user_detail=shared.UserDetail(
        email='Caden82@hotmail.com',
        full_name='Example user',
        password='AKjhdakjsdh@!34',
    ),
), token='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `signup_user_payload`                                                          | [Optional[shared.SignupUserPayload]](../../models/shared/signupuserpayload.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `token`                                                                        | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Invitation partner token                                                       |


### Response

**[operations.SignUpUserResponse](../../models/operations/signupuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_user_v2

Update user details

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.update_user_v2(id='string', user_v2=shared.UserV2(
    created_at='2022-02-08T04:44:32.246Z',
    department='Sales',
    display_name='Example User',
    favorites={
        "entity_views": 'string',
        "dashboard": 'string',
    },
    image_uri=shared.UserV2ImageURI(
        additional_properties={
            "original": 'string',
            "thumbnail_32": 'string',
        },
    ),
    is_signature_enabled=True,
    mfa_enabled=False,
    phone='1234567890',
    phone_verified=True,
    preferred_language='de',
    properties=[
        shared.UserV2Properties(
            name='profileImageName',
            value='avatar.png',
        ),
    ],
    signature='<p>Thanks</p>',
    token='65dc527f-cb2d-4158-8f2e-8978dbceb599',
))

if res.user_v2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The Id of user                                           |
| `user_v2`                                                | [Optional[shared.UserV2]](../../models/shared/userv2.md) | :heavy_minus_sign:                                       | N/A                                                      |


### Response

**[operations.UpdateUserV2Response](../../models/operations/updateuserv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## verify_email_with_token

Update new email using an verification token

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.user_v2.verify_email_with_token(token='string', user_verification_payload=shared.UserVerificationPayload(
    password='AKjhdakjsdh@!34',
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `token`                                                                                    | *str*                                                                                      | :heavy_check_mark:                                                                         | Verification Token                                                                         |
| `user_verification_payload`                                                                | [Optional[shared.UserVerificationPayload]](../../models/shared/userverificationpayload.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |


### Response

**[operations.VerifyEmailWithTokenResponse](../../models/operations/verifyemailwithtokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
