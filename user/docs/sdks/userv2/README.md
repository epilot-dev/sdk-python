# UserV2

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
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ActivateUserRequest(
    user_activation_payload=shared.UserActivationPayload(
        display_name='Example User',
        password='AKjhdakjsdh@!34',
    ),
    token='at',
)

res = s.user_v2.activate_user(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ActivateUserRequest](../../models/operations/activateuserrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ActivateUserResponse](../../models/operations/activateuserresponse.md)**


## delete_user_v2

Delete user by user id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteUserV2Request(
    id='f7cc78ca-1ba9-428f-8816-742cb7392059',
)

res = s.user_v2.delete_user_v2(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteUserV2Request](../../models/operations/deleteuserv2request.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteUserV2Response](../../models/operations/deleteuserv2response.md)**


## get_me_v2

Get currently logged in user

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.user_v2.get_me_v2()

if res.user_v2 is not None:
    # handle response
```


### Response

**[operations.GetMeV2Response](../../models/operations/getmev2response.md)**


## get_user_login_parameters_v2

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetUserLoginParametersV2Request(
    username='Camden61',
)

res = s.user_v2.get_user_login_parameters_v2(req)

if res.get_user_login_parameters_v2_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetUserLoginParametersV2Request](../../models/operations/getuserloginparametersv2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetUserLoginParametersV2Response](../../models/operations/getuserloginparametersv2response.md)**


## get_user_v2

Get user details by user id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetUserV2Request(
    id='6fea7596-eb10-4faa-a235-2c5955907aff',
)

res = s.user_v2.get_user_v2(req)

if res.user_v2 is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetUserV2Request](../../models/operations/getuserv2request.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetUserV2Response](../../models/operations/getuserv2response.md)**


## invite_user

Creates a new user in the caller's organization and sends an invite email to activate

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.UserInvitationPayload(
    email='test@example.com',
    language=shared.UserInvitationPayloadLanguage.EN,
    roles=[
        '123:owner',
    ],
)

res = s.user_v2.invite_user(req)

if res.user_v2 is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.UserInvitationPayload](../../models/shared/userinvitationpayload.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.InviteUserResponse](../../models/operations/inviteuserresponse.md)**


## list_users_v2

Get the list of organization users

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ListUsersV2Request(
    limit=6527.9,
    offset=2088.76,
    query='culpa',
)

res = s.user_v2.list_users_v2(req)

if res.list_users_v2_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUsersV2Request](../../models/operations/listusersv2request.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListUsersV2Response](../../models/operations/listusersv2response.md)**


## resend_user_invitation

Resend user invitation email

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ResendUserInvitationRequestBody(
    email='test@example.com',
    language=operations.ResendUserInvitationRequestBodyLanguage.EN,
)

res = s.user_v2.resend_user_invitation(req)

if res.user_v2 is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ResendUserInvitationRequestBody](../../models/operations/resenduserinvitationrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ResendUserInvitationResponse](../../models/operations/resenduserinvitationresponse.md)**


## sign_up_user

signUpUser

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.SignUpUserRequest(
    signup_user_payload=shared.SignupUserPayload(
        language=shared.SignupUserPayloadLanguage.DE,
        organization_detail={
            "mollitia": 'occaecati',
        },
        user_detail=shared.UserDetail(
            email='Harvey.Konopelski@gmail.com',
            full_name='Example user',
            password='AKjhdakjsdh@!34',
        ),
    ),
    token='error',
)

res = s.user_v2.sign_up_user(req)

if res.sign_up_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.SignUpUserRequest](../../models/operations/signupuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.SignUpUserResponse](../../models/operations/signupuserresponse.md)**


## update_user_v2

Update user details

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateUserV2Request(
    user_v2=shared.UserV2(
        created_at='2022-02-08T04:44:32.246Z',
        department='Sales',
        display_name='Example User',
        draft_email='Eugene_Brown31@gmail.com',
        email='Orlando.Dietrich66@gmail.com',
        favorites={
            "possimus": 'aut',
        },
        id='19da1ffe-78f0-497b-8074-f15471b5e6e1',
        image_uri={
            "ipsum": 'quidem',
        },
        is_signature_enabled=True,
        mfa_enabled=False,
        organization_id='molestias',
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
        status=shared.UserV2Status.DEACTIVATED,
        token='65dc527f-cb2d-4158-8f2e-8978dbceb599',
    ),
    id='d488e1e9-1e45-40ad-aabd-44269802d502',
)

res = s.user_v2.update_user_v2(req)

if res.user_v2 is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateUserV2Request](../../models/operations/updateuserv2request.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateUserV2Response](../../models/operations/updateuserv2response.md)**


## verify_email_with_token

Update new email using an verification token

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.VerifyEmailWithTokenRequest(
    user_verification_payload=shared.UserVerificationPayload(
        password='AKjhdakjsdh@!34',
    ),
    token='dolorum',
)

res = s.user_v2.verify_email_with_token(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.VerifyEmailWithTokenRequest](../../models/operations/verifyemailwithtokenrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.VerifyEmailWithTokenResponse](../../models/operations/verifyemailwithtokenresponse.md)**

