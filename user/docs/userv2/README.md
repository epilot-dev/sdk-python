# user_v2

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
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ActivateUserRequest(
    user_activation_payload=shared.UserActivationPayload(
        display_name='Example User',
        password='AKjhdakjsdh@!34',
    ),
    token='maiores',
)

res = s.user_v2.activate_user(req)

if res.status_code == 200:
    # handle response
```

## delete_user_v2

Delete user by user id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DeleteUserV2Request(
    id='7cc78ca1-ba92-48fc-8167-42cb73920592',
)

res = s.user_v2.delete_user_v2(req)

if res.user is not None:
    # handle response
```

## get_me_v2

Get currently logged in user

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.user_v2.get_me_v2()

if res.user_v2 is not None:
    # handle response
```

## get_user_login_parameters_v2

Get user organization login parameters by username

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetUserLoginParametersV2Request(
    username='Leora.Fadel',
)

res = s.user_v2.get_user_login_parameters_v2(req)

if res.get_user_login_parameters_v2_200_application_json_object is not None:
    # handle response
```

## get_user_v2

Get user details by user id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetUserV2Request(
    id='fea7596e-b10f-4aaa-a352-c5955907aff1',
)

res = s.user_v2.get_user_v2(req)

if res.user_v2 is not None:
    # handle response
```

## invite_user

Creates a new user in the caller's organization and sends an invite email to activate

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.UserInvitationPayload(
    email='test@example.com',
    language=shared.UserInvitationPayloadLanguageEnum.DE,
    roles=[
        '123:owner',
    ],
)

res = s.user_v2.invite_user(req)

if res.user_v2 is not None:
    # handle response
```

## list_users_v2

Get the list of organization users

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListUsersV2Request(
    limit=6350.59,
    offset=1613.09,
    query='repellat',
)

res = s.user_v2.list_users_v2(req)

if res.list_users_v2_200_application_json_object is not None:
    # handle response
```

## resend_user_invitation

Resend user invitation email

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ResendUserInvitationRequestBody(
    email='test@example.com',
    language=operations.ResendUserInvitationRequestBodyLanguageEnum.DE,
)

res = s.user_v2.resend_user_invitation(req)

if res.user_v2 is not None:
    # handle response
```

## sign_up_user

signUpUser

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.SignUpUserRequest(
    signup_user_payload=shared.SignupUserPayload(
        language=shared.SignupUserPayloadLanguageEnum.DE,
        organization_detail={
            "commodi": 'quam',
            "molestiae": 'velit',
        },
        user_detail=shared.UserDetail(
            email='Carmelo67@yahoo.com',
            full_name='Example user',
            password='AKjhdakjsdh@!34',
        ),
    ),
    token='animi',
)

res = s.user_v2.sign_up_user(req)

if res.sign_up_user_200_application_json_object is not None:
    # handle response
```

## update_user_v2

Update user details

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdateUserV2Request(
    user_v2=shared.UserV2(
        created_at='2022-02-08T04:44:32.246Z',
        department='Sales',
        display_name='Example User',
        draft_email='Britney94@gmail.com',
        email='Makayla9@yahoo.com',
        id='9da1ffe7-8f09-47b0-874f-15471b5e6e13',
        image_uri={
            "molestias": 'excepturi',
            "pariatur": 'modi',
            "praesentium": 'rem',
        },
        is_signature_enabled=True,
        mfa_enabled=False,
        organization_id='voluptates',
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
        status=shared.UserV2StatusEnum.DELETED,
        token='65dc527f-cb2d-4158-8f2e-8978dbceb599',
    ),
    id='91e450ad-2abd-4442-a980-2d502a94bb4f',
)

res = s.user_v2.update_user_v2(req)

if res.user_v2 is not None:
    # handle response
```

## verify_email_with_token

Update new email using an verification token

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.VerifyEmailWithTokenRequest(
    user_verification_payload=shared.UserVerificationPayload(
        password='AKjhdakjsdh@!34',
    ),
    token='eum',
)

res = s.user_v2.verify_email_with_token(req)

if res.status_code == 200:
    # handle response
```
