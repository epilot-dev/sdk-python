# UserV2SDK
(*user_v2*)

## Overview

User API V2

### Available Operations

* [activate_user](#activate_user) - activateUser
* [check_invite_token](#check_invite_token) - checkInviteToken
* [delete_user_v2](#delete_user_v2) - deleteUserV2
* [get_groups_for_user](#get_groups_for_user) - getGroupsForUser
* [get_me_v2](#get_me_v2) - getMeV2
* [get_user_login_parameters_v2](#get_user_login_parameters_v2) - getUserLoginParametersV2
* [get_user_v2](#get_user_v2) - getUserV2
* [invite_user](#invite_user) - inviteUser
* [list_users_v2](#list_users_v2) - listUsersV2
* [reject_invite](#reject_invite) - rejectInvite
* [resend_user_invitation](#resend_user_invitation) - resendUserInvitation
* [sign_up_user](#sign_up_user) - signUpUser
* [switch_organization](#switch_organization) - switchOrganization
* [update_user_v2](#update_user_v2) - updateUserV2
* [verify_email_with_token](#verify_email_with_token) - verifyEmailWithToken

## activate_user

Activate user using an invite token

### Example Usage

```python
from epilot_user import Epilot

with Epilot() as epilot:

    epilot.user_v2.activate_user(token="<value>", display_name="Example User", password="AKjhdakjsdh@!34")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Invite Token                                                        |                                                                     |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | User's display name (default: email address)                        | Example User                                                        |
| `password`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | User's password                                                     | AKjhdakjsdh@!34                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## check_invite_token

Check an invite token

### Example Usage

```python
from epilot_user import Epilot

with Epilot() as epilot:

    res = epilot.user_v2.check_invite_token(token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Invite Token                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckInviteTokenResponseBody](../../models/checkinvitetokenresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_user_v2

Delete user by user id

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.delete_user_v2(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.User](../../models/user.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_groups_for_user

Get groups of a user

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.get_groups_for_user(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Group]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_me_v2

Get currently logged in user

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.get_me_v2()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserV2](../../models/userv2.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_user_login_parameters_v2

Get user organization login parameters by username

The first item in the list corresponds to the user's primary organization and must be used for initial login.


### Example Usage

```python
from epilot_user import Epilot

with Epilot() as epilot:

    res = epilot.user_v2.get_user_login_parameters_v2(username="Eve94")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Username                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserLoginParametersV2ResponseBody](../../models/getuserloginparametersv2responsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_user_v2

Get user details by user id

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.get_user_v2(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of user                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserV2](../../models/userv2.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## invite_user

Creates a new user in the caller's organization and sends an invite email to activate the user


### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.invite_user(request={
        "email": "test@example.com",
        "roles": [
            "123:owner",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UserInvitationPayload](../../models/userinvitationpayload.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UserV2](../../models/userv2.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_users_v2

Get the list of organization users

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.list_users_v2()

    # Handle response
    print(res)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reject_invite

Reject an invite

### Example Usage

```python
from epilot_user import Epilot

with Epilot() as epilot:

    res = epilot.user_v2.reject_invite(token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Invite Token                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RejectInviteResponseBody](../../models/rejectinviteresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## resend_user_invitation

Resend user invitation email

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.resend_user_invitation(request={
        "email": "test@example.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.ResendUserInvitationRequestBody](../../models/resenduserinvitationrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.UserV2](../../models/userv2.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## sign_up_user

signUpUser

### Example Usage

```python
import epilot_user
from epilot_user import Epilot

with Epilot() as epilot:

    res = epilot.user_v2.sign_up_user(signup_user_payload=epilot_user.SignupUserPayload(
        organization_detail=epilot_user.OrganizationDetail(
            email="Abbie.Runolfsson82@yahoo.com",
            name="Epilot",
            pricing_tier="professional",
            type=epilot_user.OrganizationDetailType.VENDOR,
            is_privacy_policy_checked=False,
            is_terms_and_conditions_checked=False,
            **{

            },
        ),
        user_detail={
            "email": "Brown.Zulauf-Ruecker@yahoo.com",
            "full_name": "Example user",
            "password": "AKjhdakjsdh@!34",
        },
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `token`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Partner invitation token                                                |
| `signup_user_payload`                                                   | [Optional[models.SignupUserPayload]](../../models/signupuserpayload.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SignUpUserResponseBody](../../models/signupuserresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## switch_organization

Switch to another organization the user is part of

### Example Usage

```python
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.switch_organization()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.SwitchOrganizationRequestBody](../../models/switchorganizationrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SwitchOrganizationResponseBody](../../models/switchorganizationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_user_v2

Update user details

### Example Usage

```python
import epilot_user
from epilot_user import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.user_v2.update_user_v2(id="<id>", department="Sales", display_name="Example User", email_notification_setting={
        "added_participant_opportunity": True,
        "assigned_opportunity": True,
        "assigned_task": True,
        "comment_opportunity": True,
        "deleted_task": True,
        "escalated_task": True,
        "message_receive_opportunity": True,
        "message_send_opportunity": True,
        "created_task": True,
        "created_opportunity_manual": True,
        "created_opportunity_auto": True,
        "deleted_opportunity": True,
    }, favorites={
        "entity_views": {
            "opportunity": "891a5409850abf8b92bd2cb7bdd2844d32ce6bec",
            "order": "628aee91-7c2f-4047-ab0d-433582a19c49",
        },
        "dashboard": "751ff121-9ac2-4511-a2e6-851f11287380",
    }, feature_preferences={
        "feature_name": True,
    }, image_uri=epilot_user.UserV2ImageURI(
        original="https://account-profile-images.epilot.cloud/1/avatar.png",
        thumbnail_32="https://account-profile-images.epilot.cloud/1/avatar_32x32.png",
        **{

        },
    ), is_signature_enabled=True, mfa_enabled=False, phone="1234567890", phone_verified=True, preferred_language="de", properties=[
        {
            "name": "profileImageName",
            "value": "avatar.png",
        },
        {
            "name": "profileImageName",
            "value": "avatar.png",
        },
        {
            "name": "profileImageName",
            "value": "avatar.png",
        },
    ], secondary_phone="1234567890", signature="<p>Thanks</p>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                        | The Id of user                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                           |
| `activated_at`                                                                                                                                                                                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |
| `created_at`                                                                                                                                                                                                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |
| `custom_start_page`                                                                                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's start page after login                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                           |
| `department`                                                                                                                                                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's department                                                                                                                                                                                                                                                                                                                                                         | Sales                                                                                                                                                                                                                                                                                                                                                                     |
| `display_name`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's display name (default: email address)                                                                                                                                                                                                                                                                                                                              | Example User                                                                                                                                                                                                                                                                                                                                                              |
| `draft_email`                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's pending email address                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                           |
| `email`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's email address                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                           |
| `email_notification_setting`                                                                                                                                                                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       | {<br/>"added_participant_opportunity": true,<br/>"assigned_opportunity": true,<br/>"assigned_task": true,<br/>"comment_opportunity": true,<br/>"deleted_task": true,<br/>"escalated_task": true,<br/>"message_receive_opportunity": true,<br/>"message_send_opportunity": true,<br/>"created_task": true,<br/>"created_opportunity_manual": true,<br/>"created_opportunity_auto": true,<br/>"deleted_opportunity": true<br/>} |
| `favorites`                                                                                                                                                                                                                                                                                                                                                               | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       | {<br/>"entity_views": {<br/>"opportunity": "891a5409850abf8b92bd2cb7bdd2844d32ce6bec",<br/>"order": "628aee91-7c2f-4047-ab0d-433582a19c49"<br/>},<br/>"dashboard": "751ff121-9ac2-4511-a2e6-851f11287380"<br/>}                                                                                                                                                           |
| `feature_preferences`                                                                                                                                                                                                                                                                                                                                                     | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's feature preferences                                                                                                                                                                                                                                                                                                                                                | {<br/>"feature_name": true<br/>}                                                                                                                                                                                                                                                                                                                                          |
| `image_uri`                                                                                                                                                                                                                                                                                                                                                               | [OptionalNullable[models.UserV2ImageURI]](../../models/userv2imageuri.md)                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's custom profile image                                                                                                                                                                                                                                                                                                                                               | {<br/>"original": "https://account-profile-images.epilot.cloud/1/avatar.png",<br/>"thumbnail_32": "https://account-profile-images.epilot.cloud/1/avatar_32x32.png"<br/>}                                                                                                                                                                                                  |
| `is_signature_enabled`                                                                                                                                                                                                                                                                                                                                                    | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Whether the user's signature is enabled                                                                                                                                                                                                                                                                                                                                   | true                                                                                                                                                                                                                                                                                                                                                                      |
| `mfa_enabled`                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's multi-factor authentication status                                                                                                                                                                                                                                                                                                                                 | false                                                                                                                                                                                                                                                                                                                                                                     |
| `organization_id`                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |
| `override_release_channel`                                                                                                                                                                                                                                                                                                                                                | [OptionalNullable[models.OverrideReleaseChannel]](../../models/overridereleasechannel.md)                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | This field is used to override the release channel for the user.                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                           |
| `phone`                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's phone number                                                                                                                                                                                                                                                                                                                                                       | 1234567890                                                                                                                                                                                                                                                                                                                                                                |
| `phone_verified`                                                                                                                                                                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's phone number verification status                                                                                                                                                                                                                                                                                                                                   | true                                                                                                                                                                                                                                                                                                                                                                      |
| `preferred_language`                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's preferred language                                                                                                                                                                                                                                                                                                                                                 | de                                                                                                                                                                                                                                                                                                                                                                        |
| `properties`                                                                                                                                                                                                                                                                                                                                                              | List[[models.UserV2Properties](../../models/userv2properties.md)]                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |
| `secondary_phone`                                                                                                                                                                                                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's secondary phone number, preferred for communication                                                                                                                                                                                                                                                                                                                | 1234567890                                                                                                                                                                                                                                                                                                                                                                |
| `signature`                                                                                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | User's email signature                                                                                                                                                                                                                                                                                                                                                    | <p>Thanks</p>                                                                                                                                                                                                                                                                                                                                                             |
| `status`                                                                                                                                                                                                                                                                                                                                                                  | [Optional[models.Status]](../../models/status.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |
| `token`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Token used to invite a user to epilot                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.UserV2](../../models/userv2.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## verify_email_with_token

Update new email using an verification token

### Example Usage

```python
from epilot_user import Epilot

with Epilot() as epilot:

    epilot.user_v2.verify_email_with_token(token="<value>", password="AKjhdakjsdh@!34")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Verification Token                                                  |                                                                     |
| `password`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | User's password                                                     | AKjhdakjsdh@!34                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |