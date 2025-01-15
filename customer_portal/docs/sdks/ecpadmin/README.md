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
* [get_portal_extensions](#get_portal_extensions) - getPortalExtensions
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_recipients_to_notify_on_automation](#get_recipients_to_notify_on_automation) - getRecipientsToNotifyOnAutomation
* [get_registration_identifiers](#get_registration_identifiers) - getRegistrationIdentifiers
* [get_resolved_external_link](#get_resolved_external_link) - getResolvedExternalLink
* [get_valid_secondary_attributes](#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](#replace_ecp_template_variables) - replaceECPTemplateVariables
* [resend_confirmation_email](#resend_confirmation_email) - resendConfirmationEmail
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

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.can_trigger_portal_flow(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, activity_id="01F130Q52Q6MWSNS8N2AVXV4JN", ecp_config={
        "file_config": {
            "tags": [
                "example",
                "mock",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `activity_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Id of the activity                                                  | 01F130Q52Q6MWSNS8N2AVXV4JN                                          |
| `ecp_config`                                                        | [Optional[models.EcpConfig]](../../models/ecpconfig.md)             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CanTriggerPortalFlowResponseBody](../../models/cantriggerportalflowresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## configure_distribution

Configure the distribution for the portal's custom domain

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.configure_distribution(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureDistributionResponseBody](../../models/configuredistributionresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## create_sso_user

Creates a portal user as an SSO user.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.create_sso_user(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, email="testemail921@yopmail.com", first_name="John", last_name="Doe")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | User's email address                                                | testemail921@yopmail.com                                            |
| `first_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | First Name of the portal user                                       | John                                                                |
| `last_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Last Name of the portal user                                        | Doe                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateSSOUserResponseBody](../../models/createssouserresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## delete_portal

Deletes the portal.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.ecp_admin.delete_portal(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## extra_permission_attributes

Retrieves the extra permission attributes.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.extra_permission_attributes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ExtraPermissionAttributesResponseBody](../../models/extrapermissionattributesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## fetch_portal_users_by_related_entity

Get all users for a given entity

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.fetch_portal_users_by_related_entity(entity_id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT)

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_all_portal_configs

Retrieves all portal configurations.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_all_portal_configs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllPortalConfigsResponseBody](../../models/getallportalconfigsresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_ecp_contact

Get the Contact by id

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_ecp_contact(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetECPContactResponseBody](../../models/getecpcontactresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 401, 403, 404, 500 | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## get_email_templates

Retrieves the email templates of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_email_templates(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmailTemplates](../../models/emailtemplates.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_entity_identifiers

Retrieve a list of entity identifiers used for entity search by portal users.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_entity_identifiers(slug=epilot_customer_portal.EntitySlug.CONTACT)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slug`                                                              | [models.EntitySlug](../../models/entityslug.md)                     | :heavy_check_mark:                                                  | The slug of an entity                                               | contact                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetEntityIdentifiersResponseBody](../../models/getentityidentifiersresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_external_links

Retrieves the portal configuration external links.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_external_links(contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.ExternalLink]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_org_portal_config

Retrieves the portal configuration for the organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_org_portal_config(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOrgPortalConfigResponseBody](../../models/getorgportalconfigresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_portal_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PortalConfig](../../models/portalconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_extensions

Retrieves the installed portal extensions.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_portal_extensions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Extension]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_portal_widgets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_recipients_to_notify_on_automation

Get recipients to notify on automation

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_recipients_to_notify_on_automation(request={
        "emails": [
            "john@doe.com",
        ],
        "template_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.GetRecipientsToNotifyOnAutomationRequestBody](../../models/getrecipientstonotifyonautomationrequestbody.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.GetRecipientsToNotifyOnAutomationResponseBody](../../models/getrecipientstonotifyonautomationresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_registration_identifiers

Get valid attributes from entities that can be used as identifier to map contact to user on registration

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_registration_identifiers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRegistrationIdentifiersResponseBody](../../models/getregistrationidentifiersresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_resolved_external_link

Retrieves a resolved portal external link.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_resolved_external_link(id="5da0a718-c822-403d-9f5d-20d4584e0528", contact_id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the External Link                                             | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `contact_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact ID of the user                                              | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `origin`                                                            | [Optional[models.Origin]](../../models/origin.md)                   | :heavy_minus_sign:                                                  | Origin of the portal                                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ExternalLink](../../models/externallink.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_valid_secondary_attributes

Get valid secondary attributes that are used while mapping a contact on registration

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.get_valid_secondary_attributes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetValidSecondaryAttributesResponseBody](../../models/getvalidsecondaryattributesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## login_to_portal_as_user

Generate a token to log in to a portal impersonating a users.

Token is valid for 5 minutes.


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.login_to_portal_as_user(request={
        "email": "portal-customer@email.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.LoginToPortalAsUserRequestBody](../../models/logintoportalasuserrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.LoginToPortalAsUserResponseBody](../../models/logintoportalasuserresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## replace_ecp_template_variables

Replaces the template variables of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.replace_ecp_template_variables(request={
        "key": {
            "id": "5da0a718-c822-403d-9f5d-20d4584e0528",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Dict[str, models.RequestBody]](../../models/.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReplaceECPTemplateVariablesResponseBody](../../models/replaceecptemplatevariablesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 500         | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## resend_confirmation_email

Resend confirmation email

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.resend_confirmation_email(id="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of portal user id                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ResendConfirmationEmailResponseBody](../../models/resendconfirmationemailresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 400, 401, 404, 500 | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## save_portal_files

Add files to portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.save_portal_files(files=[
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
    ], origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `files`                                                                 | List[[models.SavePortalFileFiles](../../models/saveportalfilefiles.md)] | :heavy_check_mark:                                                      | N/A                                                                     |
| `origin`                                                                | [models.Origin](../../models/origin.md)                                 | :heavy_check_mark:                                                      | Origin of the portal                                                    |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SavePortalFilesResponseBody](../../models/saveportalfilesresponsebody.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ErrorResp        | 400, 401, 403, 404, 500 | application/json        |
| models.APIError         | 4XX, 5XX                | \*/\*                   |

## upsert_email_templates

Upserts the email templates of a portal

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.upsert_email_templates(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, advanced_mfa="5da0a718-c822-403d-9f5d-20d4584e0528", confirm_account="5da0a718-c822-403d-9f5d-20d4584e0528", confirm_email_update="5da0a718-c822-403d-9f5d-20d4584e0528", forgot_password="5da0a718-c822-403d-9f5d-20d4584e0528", invitation="5da0a718-c822-403d-9f5d-20d4584e0528", on_doc_upload="5da0a718-c822-403d-9f5d-20d4584e0528", on_map_a_pending_user="5da0a718-c822-403d-9f5d-20d4584e0528", on_new_quote="5da0a718-c822-403d-9f5d-20d4584e0528", on_workflow_step_assigned="5da0a718-c822-403d-9f5d-20d4584e0528")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |                                                                     |
| `advanced_mfa`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `confirm_account`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `confirm_email_update`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `forgot_password`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `invitation`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `on_doc_upload`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `on_map_a_pending_user`                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `on_new_quote`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `on_workflow_step_assigned`                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity ID                                                           | 5da0a718-c822-403d-9f5d-20d4584e0528                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpsertEmailTemplatesResponseBody](../../models/upsertemailtemplatesresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401, 403, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## upsert_portal

Upserts the settings for a portal of an organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.upsert_portal(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, config="<value>", design_id="5da0a718-c822-403d-9f5d-20d4584e0528", feature_settings={}, allowed_file_extensions={
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
    }, approval_state_attributes={
        "contact": [
            "name",
            "address",
        ],
        "contract": [
            "installment_amount",
        ],
    }, cognito_details={
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
    }, contract_identifiers=[
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
            "schema_": epilot_customer_portal.EntitySlug.CONTACT,
        },
    ], default_user_to_notify={
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
                **{

                },
            ),
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
                **{

                },
            ),
        ],
    }, domain="abc.com", email_templates={
        "advanced_mfa": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "confirm_account": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "confirm_email_update": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "forgot_password": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "invitation": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_doc_upload": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_map_a_pending_user": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_new_quote": "5da0a718-c822-403d-9f5d-20d4584e0528",
        "on_workflow_step_assigned": "5da0a718-c822-403d-9f5d-20d4584e0528",
    }, entity_actions=[
        {
            "journey_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
            "slug": epilot_customer_portal.EntitySlug.CONTACT,
        },
        {
            "journey_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
            "slug": epilot_customer_portal.EntitySlug.CONTACT,
        },
    ], entity_edit_rules=[
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
    ], images={
        "order_left_teaser": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-left-teaser.jpeg",
        "order_right_teaser": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-right-teaser.jpeg",
        "welcome_banner": "https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/welcome-banner.jpeg",
    }, name="Installer Portal", registration_identifiers=[
        {
            "name": "last_name",
            "schema_": epilot_customer_portal.EntitySlug.CONTACT,
        },
        {
            "name": "contract_number",
            "schema_": epilot_customer_portal.EntitySlug.CONTACT,
        },
    ], triggered_journeys=[
        {
            "journey_id": "5da0a718-c822-403d-9f5d-20d4584e0528",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `origin`                                                                                                                                                                                                                        | [models.Origin](../../models/origin.md)                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                              | Origin of the portal                                                                                                                                                                                                            |                                                                                                                                                                                                                                 |
| `config`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | Stringified object with configuration details                                                                                                                                                                                   |                                                                                                                                                                                                                                 |
| `design_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | Entity ID                                                                                                                                                                                                                       | 5da0a718-c822-403d-9f5d-20d4584e0528                                                                                                                                                                                            |
| `feature_settings`                                                                                                                                                                                                              | [models.UpsertPortalConfigFeatureSettings](../../models/upsertportalconfigfeaturesettings.md)                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                              | Feature settings for the portal                                                                                                                                                                                                 |                                                                                                                                                                                                                                 |
| `access_token`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Access token for the portal                                                                                                                                                                                                     |                                                                                                                                                                                                                                 |
| `advanced_mfa`                                                                                                                                                                                                                  | [Optional[models.UpsertPortalConfigAdvancedMfa]](../../models/upsertportalconfigadvancedmfa.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                             |                                                                                                                                                                                                                                 |
| `allowed_file_extensions`                                                                                                                                                                                                       | [Optional[models.AllowedFileExtensions]](../../models/allowedfileextensions.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Allowed file extensions for upload                                                                                                                                                                                              |                                                                                                                                                                                                                                 |
| `approval_state_attributes`                                                                                                                                                                                                     | Dict[str, List[*str*]]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                             | {<br/>"contact": [<br/>"name",<br/>"address"<br/>],<br/>"contract": [<br/>"installment_amount"<br/>]<br/>}                                                                                                                      |
| `cognito_details`                                                                                                                                                                                                               | [Optional[models.UpsertPortalConfigCognitoDetails]](../../models/upsertportalconfigcognitodetails.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                              | AWS Cognito Pool details for the portal                                                                                                                                                                                         |                                                                                                                                                                                                                                 |
| `contact_identifiers`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated. Use registration_identifiers instead.                                              | [<br/>"email",<br/>"last_name"<br/>]                                                                                                                                                                                            |
| `contract_identifiers`                                                                                                                                                                                                          | List[[models.ContractIdentifier](../../models/contractidentifier.md)]                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                              | Identifiers to identify a contract by a portal user.                                                                                                                                                                            | [<br/>{<br/>"name": "email",<br/>"schema": "contact"<br/>},<br/>{<br/>"name": "last_name",<br/>"schema": "contact"<br/>},<br/>{<br/>"name": "contract_number",<br/>"schema": "contract"<br/>}<br/>]                             |
| `default_user_to_notify`                                                                                                                                                                                                        | [Optional[models.DefaultUserToNotify]](../../models/defaultusertonotify.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | Default 360 user to notify upon an internal notification                                                                                                                                                                        |                                                                                                                                                                                                                                 |
| `domain`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The URL on which the portal is accessible                                                                                                                                                                                       | abc.com                                                                                                                                                                                                                         |
| `email_templates`                                                                                                                                                                                                               | [Optional[models.EmailTemplates]](../../models/emailtemplates.md)                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                              | Email templates used for authentication and internal processes                                                                                                                                                                  |                                                                                                                                                                                                                                 |
| `enabled`                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Enable/Disable the portal access                                                                                                                                                                                                |                                                                                                                                                                                                                                 |
| `entity_actions`                                                                                                                                                                                                                | List[[models.EntityActions](../../models/entityactions.md)]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | Journey actions allowed on an entity by a portal user                                                                                                                                                                           |                                                                                                                                                                                                                                 |
| `entity_edit_rules`                                                                                                                                                                                                             | List[[models.UpsertPortalConfigEntityEditRules](../../models/upsertportalconfigentityeditrules.md)]                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                              | Rules for editing an entity by a portal user                                                                                                                                                                                    |                                                                                                                                                                                                                                 |
| `entity_identifiers`                                                                                                                                                                                                            | [Optional[models.UpsertPortalConfigEntityIdentifiers]](../../models/upsertportalconfigentityidentifiers.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Identifiers used to identify an entity by a portal user. Deprecated. Use contract_identifiers instead. |                                                                                                                                                                                                                                 |
| `extensions`                                                                                                                                                                                                                    | List[[models.ExtensionConfig](../../models/extensionconfig.md)]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Configured Portal extensions                                                                                                                                                                                                    |                                                                                                                                                                                                                                 |
| `images`                                                                                                                                                                                                                        | [Optional[models.UpsertPortalConfigImages]](../../models/upsertportalconfigimages.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                              | Teaser & Banner Image web links                                                                                                                                                                                                 |                                                                                                                                                                                                                                 |
| `is_epilot_domain`                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Mark true if the domain is an Epilot domain                                                                                                                                                                                     |                                                                                                                                                                                                                                 |
| `name`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | A short name to identify your portal                                                                                                                                                                                            | Installer Portal                                                                                                                                                                                                                |
| `registration_identifiers`                                                                                                                                                                                                      | List[[models.ContractIdentifier](../../models/contractidentifier.md)]                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                              | Identifiers to identify a contact of a portal user during the registration.                                                                                                                                                     | [<br/>{<br/>"name": "last_name",<br/>"schema": "contact"<br/>},<br/>{<br/>"name": "contract_number",<br/>"schema": "contract"<br/>}<br/>]                                                                                       |
| `self_registration_setting`                                                                                                                                                                                                     | [Optional[models.UpsertPortalConfigSelfRegistrationSetting]](../../models/upsertportalconfigselfregistrationsetting.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                             |                                                                                                                                                                                                                                 |
| `triggered_journeys`                                                                                                                                                                                                            | List[[models.UpsertPortalConfigTriggeredJourneys](../../models/upsertportalconfigtriggeredjourneys.md)]                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                              | Journeys automatically opened on a portal user action                                                                                                                                                                           |                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                             |                                                                                                                                                                                                                                 |

### Response

**[models.PortalConfig](../../models/portalconfig.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 400, 401, 403, 500 | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |

## upsert_portal_widget

Upsert widget for a portal of an organization.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.ecp_admin.upsert_portal_widget(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL, widgets=[
        {
            "id": "<id>",
            "list_index": 253590,
            "type": epilot_customer_portal.TeaserWidgetType.METER_CHART_WIDGET,
        },
        {
            "id": "<id>",
            "list_index": 271617,
            "type": epilot_customer_portal.TeaserWidgetType.PAYMENT_WIDGET,
        },
        {
            "id": "<id>",
            "list_index": 291441,
            "type": epilot_customer_portal.TeaserWidgetType.TEASER_WIDGET,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `origin`                                                            | [models.Origin](../../models/origin.md)                             | :heavy_check_mark:                                                  | Origin of the portal                                                |
| `widgets`                                                           | List[*Any*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpsertPortalWidget](../../models/upsertportalwidget.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ErrorResp   | 400, 401, 403, 500 | application/json   |
| models.APIError    | 4XX, 5XX           | \*/\*              |