# ECPAdmin
(*ecp_admin*)

## Overview

APIs defined for a ECP Admin

### Available Operations

* [can_trigger_portal_flow](#can_trigger_portal_flow) - canTriggerPortalFlow
* [configure_distribution](#configure_distribution) - configureDistribution
* [create_sso_user](#create_sso_user) - createSSOUser
* [delete_portal](#delete_portal) - deletePortal
* [extra_permission_attributes](#extra_permission_attributes) - extraPermissionAttributes
* [fetch_portal_users_by_related_entity](#fetch_portal_users_by_related_entity) - fetchPortalUsersByRelatedEntity
* [get_all_portal_configs](#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](#get_ecp_contact) - getECPContact
* [get_email_templates](#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](#get_entity_identifiers) - getEntityIdentifiers
* [get_external_links](#get_external_links) - getExternalLinks
* [get_org_portal_config](#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_recipients_to_notify_on_automation](#get_recipients_to_notify_on_automation) - getRecipientsToNotifyOnAutomation
* [get_registration_identifiers](#get_registration_identifiers) - getRegistrationIdentifiers
* [get_valid_secondary_attributes](#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](#save_portal_files) - savePortalFiles
* [upsert_email_templates](#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](#upsert_portal) - upsertPortal
* [upsert_portal_widget](#upsert_portal_widget) - upsertPortalWidget

## can_trigger_portal_flow

Returns whether the user can trigger a portal flow

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.can_trigger_portal_flow(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, trigger_portal_flow={
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `trigger_portal_flow`                                               | [models.TriggerPortalFlow](../../models/triggerportalflow.md)       | :heavy_check_mark:                                                  | Request of trigger portal flow                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CanTriggerPortalFlowResponseBody](../../models/cantriggerportalflowresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## configure_distribution

Configure the distribution for the portal's custom domain

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.configure_distribution(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ConfigureDistributionResponseBody](../../models/configuredistributionresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_sso_user

Creates a portal user as an SSO user.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.create_sso_user(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, create_sso_user_request={
    "email": "testemail921@yopmail.com",
    "first_name": "John",
    "last_name": "Doe",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `create_sso_user_request`                                           | [models.CreateSSOUserRequest](../../models/createssouserrequest.md) | :heavy_check_mark:                                                  | Portal user payload                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CreateSSOUserResponseBody](../../models/createssouserresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## delete_portal

Deletes the portal.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.ecp_admin.delete_portal(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## extra_permission_attributes

Retrieves the extra permission attributes.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.extra_permission_attributes()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ExtraPermissionAttributesResponseBody](../../models/extrapermissionattributesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## fetch_portal_users_by_related_entity

Get all users for a given entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.fetch_portal_users_by_related_entity(entity_id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entity_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `slug`                                                              | [models.EntitySlug](../../models/entityslug.md)                     | :heavy_check_mark:                                                  | URL-friendly identifier for the entity schema                       | contact                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.FetchPortalUsersByRelatedEntityResponseBody](../../models/fetchportalusersbyrelatedentityresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_all_portal_configs

Retrieves all portal configurations.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_all_portal_configs()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetAllPortalConfigsResponseBody](../../models/getallportalconfigsresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_ecp_contact

Get the Contact by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_ecp_contact(id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetECPContactResponseBody](../../models/getecpcontactresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,404,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_email_templates

Retrieves the email templates of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_email_templates(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EmailTemplates](../../models/emailtemplates.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_entity_identifiers

Retrieve a list of entity identifiers used for entity search by portal users.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_entity_identifiers(slug=epilot_customer_portal.EntitySlug.CONTACT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slug`                                                              | [models.EntitySlug](../../models/entityslug.md)                     | :heavy_check_mark:                                                  | The slug of an entity                                               | contact                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetEntityIdentifiersResponseBody](../../models/getentityidentifiersresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_external_links

Retrieves the portal configuration external links.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_external_links(contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[List[models.JourneyActions]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_org_portal_config

Retrieves the portal configuration for the organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_org_portal_config(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_portal_config()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_portal_widgets()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_recipients_to_notify_on_automation

Get recipients to notify on automation

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_recipients_to_notify_on_automation(request={
    "emails": [
        "john@doe.com",
    ],
    "template_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.GetRecipientsToNotifyOnAutomationRequestBody](../../models/getrecipientstonotifyonautomationrequestbody.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |


### Response

**[models.GetRecipientsToNotifyOnAutomationResponseBody](../../models/getrecipientstonotifyonautomationresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_registration_identifiers

Get valid attributes from entities that can be used as identifier to map contact to user on registration

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_registration_identifiers()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetRegistrationIdentifiersResponseBody](../../models/getregistrationidentifiersresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_valid_secondary_attributes

Get valid secondary attributes that are used while mapping a contact on registration

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_valid_secondary_attributes()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetValidSecondaryAttributesResponseBody](../../models/getvalidsecondaryattributesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## login_to_portal_as_user

Generate a token to log in to a portal impersonating a users.

Token is valid for 5 minutes.


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.login_to_portal_as_user(request={
    "email": "portal-customer@email.com",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.LoginToPortalAsUserRequestBody](../../models/logintoportalasuserrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |


### Response

**[models.LoginToPortalAsUserResponseBody](../../models/logintoportalasuserresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## replace_ecp_template_variables

Replaces the template variables of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.replace_ecp_template_variables(request={
    "key": {
        "id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, models.RequestBody]](../../models/.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ReplaceECPTemplateVariablesResponseBody](../../models/replaceecptemplatevariablesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## save_portal_files

Add files to portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.save_portal_files(request={
    "files": [
        {
            "file_type": "orderRightTeaser",
            "tags": [
                "12345",
            ],
            "filename": "12345",
            "s3ref": {
                "bucket": "12345",
                "key": "12345",
            },
        },
    ],
    "origin": epilot_customer_portal.Origin.INSTALLER_PORTAL,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SavePortalFile](../../models/saveportalfile.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SavePortalFilesResponseBody](../../models/saveportalfilesresponsebody.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorResp    | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## upsert_email_templates

Upserts the email templates of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_email_templates(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, email_templates={
    "advanced_mfa": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "confirm_account": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "confirm_email_update": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "forgot_password": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "invitation": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "on_doc_upload": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "on_map_a_pending_user": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "on_new_quote": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "on_workflow_step_assigned": "5da0a718-c822-403d-9f5d-20d4584e0528",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `email_templates`                                                   | [models.EmailTemplates](../../models/emailtemplates.md)             | :heavy_check_mark:                                                  | Email templates payload                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpsertEmailTemplatesResponseBody](../../models/upsertemailtemplatesresponsebody.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## upsert_portal

Upserts the settings for a portal of an organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_portal(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, upsert_portal_config={
    "config": "<value>",
    "design_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "feature_settings": {},
    "allowed_file_extensions": {
        "archive": [
            "zip",
        ],
        "audio_video": [
            "mp4",
        ],
        "cad": [
            "cad",
        ],
        "calendar": [
            "ics",
        ],
        "document": [
            "pdf",
        ],
        "email": [
            "eml",
        ],
        "image": [
            "jpg",
        ],
        "other": [
            "txt",
        ],
        "presentation": [
            "ppt",
        ],
        "spreadsheet": [
            "xls",
        ],
    },
    "approval_state_attributes": {
        "contact": [
            "name",
            "address",
        ],
        "contract": [
            "installment_amount",
        ],
    },
    "cognito_details": {
        "cognito_user_pool_arn": "arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_123412341",
        "cognito_user_pool_client_id": "6bsd0jkgoie74k2i8mrhc1vest",
        "cognito_user_pool_id": "eu-central-1_CUEQRNbUb",
        "password_policy": {
            "minimum_length": 8,
            "require_lowercase": True,
            "require_numbers": True,
            "require_symbols": True,
            "require_uppercase": True,
        },
    },
    "default_user_to_notify": {
        "on_pending_user": [
            epilot_customer_portal.AdminUser(
                display_name="John",
                email="j.doe@epilot.cloud",
                image_uri={
                    "key": "fuafjvoHKsudhfagweucjasdvga",
                    "original": "https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original",
                    "thumbnail_32": "https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original?w=32&h=32",
                    "thumbnail_64": "https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original?w=64&h=64",
                },
                org_id="123",
                phone="12345 67890",
                type="user",
                user_id="123456",
            ),
        ],
    },
    "domain": "abc.com",
    "email_templates": {
        "advanced_mfa": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "confirm_account": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "confirm_email_update": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "forgot_password": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "invitation": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_doc_upload": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_map_a_pending_user": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_new_quote": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_workflow_step_assigned": "5da0a718-c822-403d-9f5d-20d4584e0528",
    },
    "entity_actions": [
        {
            "journey_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
            "slug": epilot_customer_portal.EntitySlug.CONTACT,
        },
    ],
    "entity_edit_rules": [
        {
            "allowed_decrement": "10%",
            "allowed_increment": "10%",
            "attribute": "first_name",
            "cadence_period": 1,
            "changes_allowed": 1,
            "grace_period": 1,
            "number_of_days_before_restriction": 10,
            "slug": epilot_customer_portal.EntitySlug.CONTACT,
        },
    ],
    "entity_identifiers": {
        "type": {
            "attributes": [
                "contract_number",
            ],
        },
    },
    "grants": [
        {
            "action": "entity-read",
            "resource": "entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947",
        },
    ],
    "images": {
        "order_left_teaser": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-left-teaser.jpeg",
        "order_right_teaser": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-right-teaser.jpeg",
        "welcome_banner": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/welcome-banner.jpeg",
    },
    "name": "Installer Portal",
    "registration_identifiers": [
        {
            "name": "email",
            "schema_": epilot_customer_portal.EntitySlug.CONTACT,
        },
        {
            "name": "last_name",
            "schema_": epilot_customer_portal.EntitySlug.CONTACT,
        },
        {
            "name": "contract_number",
            "schema_": epilot_customer_portal.EntitySlug.CONTRACT,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `upsert_portal_config`                                              | [models.UpsertPortalConfig](../../models/upsertportalconfig.md)     | :heavy_check_mark:                                                  | Portal payload                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.PortalConfig](../../models/portalconfig.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,403,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## upsert_portal_widget

Upsert widget for a portal of an organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_portal_widget(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, upsert_portal_widget={
    "widgets": [
        {
            "id": "<id>",
            "list_index": 195954,
            "type": epilot_customer_portal.ActionWidgetType.DOCUMENT_WIDGET,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `upsert_portal_widget`                                              | [models.UpsertPortalWidget](../../models/upsertportalwidget.md)     | :heavy_check_mark:                                                  | Portal widgets payload                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,403,500  | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
