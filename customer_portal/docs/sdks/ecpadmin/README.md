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
* [get_org_portal_config](#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_portal_widgets](#get_portal_widgets) - getPortalWidgets
* [get_registered_users](#get_registered_users) - getRegisteredUsers
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
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.can_trigger_portal_flow(trigger_portal_flow=components.TriggerPortalFlow(
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `trigger_portal_flow`                                                        | [components.TriggerPortalFlow](../../models/components/triggerportalflow.md) | :heavy_check_mark:                                                           | Request of trigger portal flow                                               |
| `origin`                                                                     | [components.Origin](../../models/components/origin.md)                       | :heavy_check_mark:                                                           | Origin of the portal                                                         |


### Response

**[operations.CanTriggerPortalFlowResponse](../../models/operations/cantriggerportalflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## configure_distribution

Configure the distribution for the portal's custom domain

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.configure_distribution(origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `origin`                                               | [components.Origin](../../models/components/origin.md) | :heavy_check_mark:                                     | Origin of the portal                                   |


### Response

**[operations.ConfigureDistributionResponse](../../models/operations/configuredistributionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## create_sso_user

Creates a portal user as an SSO user.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.create_sso_user(create_sso_user_request=components.CreateSSOUserRequest(
    email='testemail921@yopmail.com',
    first_name='John',
    last_name='Doe',
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `create_sso_user_request`                                                          | [components.CreateSSOUserRequest](../../models/components/createssouserrequest.md) | :heavy_check_mark:                                                                 | Portal user payload                                                                |
| `origin`                                                                           | [components.Origin](../../models/components/origin.md)                             | :heavy_check_mark:                                                                 | Origin of the portal                                                               |


### Response

**[operations.CreateSSOUserResponse](../../models/operations/createssouserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete_portal

Deletes the portal.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.delete_portal(origin=components.Origin.END_CUSTOMER_PORTAL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `origin`                                               | [components.Origin](../../models/components/origin.md) | :heavy_check_mark:                                     | Origin of the portal                                   |


### Response

**[operations.DeletePortalResponse](../../models/operations/deleteportalresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## extra_permission_attributes

Retrieves the extra permission attributes.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.extra_permission_attributes()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ExtraPermissionAttributesResponse](../../models/operations/extrapermissionattributesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## fetch_portal_users_by_related_entity

Get all users for a given entity

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.fetch_portal_users_by_related_entity(entity_id='5da0a718-c822-403d-9f5d-20d4584e0528', slug=components.EntitySlug.CONTACT)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `entity_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                           |
| `slug`                                                         | [components.EntitySlug](../../models/components/entityslug.md) | :heavy_check_mark:                                             | URL-friendly identifier for the entity schema                  | contact                                                        |


### Response

**[operations.FetchPortalUsersByRelatedEntityResponse](../../models/operations/fetchportalusersbyrelatedentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_all_portal_configs

Retrieves all portal configurations.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_all_portal_configs()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetAllPortalConfigsResponse](../../models/operations/getallportalconfigsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_ecp_contact

Get the Contact by id

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_ecp_contact(id='1234')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                | 1234               |


### Response

**[operations.GetECPContactResponse](../../models/operations/getecpcontactresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,404,500  | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_email_templates

Retrieves the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_email_templates(origin=components.Origin.END_CUSTOMER_PORTAL)

if res.email_templates is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `origin`                                               | [components.Origin](../../models/components/origin.md) | :heavy_check_mark:                                     | Origin of the portal                                   |


### Response

**[operations.GetEmailTemplatesResponse](../../models/operations/getemailtemplatesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_entity_identifiers

Retrieve a list of entity identifiers used for entity search by portal users.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_entity_identifiers(slug=components.EntitySlug.CONTACT)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `slug`                                                         | [components.EntitySlug](../../models/components/entityslug.md) | :heavy_check_mark:                                             | The slug of an entity                                          | contact                                                        |


### Response

**[operations.GetEntityIdentifiersResponse](../../models/operations/getentityidentifiersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_org_portal_config

Retrieves the portal configuration for the organization.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_org_portal_config(origin=components.Origin.INSTALLER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `origin`                                               | [components.Origin](../../models/components/origin.md) | :heavy_check_mark:                                     | Origin of the portal                                   |


### Response

**[operations.GetOrgPortalConfigResponse](../../models/operations/getorgportalconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_portal_config(origin=components.Origin.END_CUSTOMER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `origin`                                                         | [Optional[components.Origin]](../../models/components/origin.md) | :heavy_minus_sign:                                               | Origin of the portal                                             |


### Response

**[operations.GetPortalConfigResponse](../../models/operations/getportalconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_portal_widgets(origin=components.Origin.END_CUSTOMER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `origin`                                                         | [Optional[components.Origin]](../../models/components/origin.md) | :heavy_minus_sign:                                               | Origin of the portal                                             |


### Response

**[operations.GetPortalWidgetsResponse](../../models/operations/getportalwidgetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_registered_users

Returns the registered emails on any portal from the given emails

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetRegisteredUsersRequestBody(
    emails=[
        'john@doe.com',
    ],
)

res = s.ecp_admin.get_registered_users(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetRegisteredUsersRequestBody](../../models/operations/getregisteredusersrequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetRegisteredUsersResponse](../../models/operations/getregisteredusersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_registration_identifiers

Get valid attributes from entities that can be used as identifier to map contact to user on registration

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_registration_identifiers()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetRegistrationIdentifiersResponse](../../models/operations/getregistrationidentifiersresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_valid_secondary_attributes

Get valid secondary attributes that are used while mapping a contact on registration

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.get_valid_secondary_attributes()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetValidSecondaryAttributesResponse](../../models/operations/getvalidsecondaryattributesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## login_to_portal_as_user

Generate a token to log in to a portal impersonating a users.

Token is valid for 5 minutes.


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.LoginToPortalAsUserRequestBody(
    email='portal-customer@email.com',
)

res = s.ecp_admin.login_to_portal_as_user(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.LoginToPortalAsUserRequestBody](../../models/operations/logintoportalasuserrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.LoginToPortalAsUserResponse](../../models/operations/logintoportalasuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## replace_ecp_template_variables

Replaces the template variables of a portal

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = {
    'key': operations.RequestBody(
        id='7aa44fb8-d60e-40cc-9a3a-ba09a1ff7f51',
    ),
}

res = s.ecp_admin.replace_ecp_template_variables(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [Dict[str, operations.RequestBody]](../../models/.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[operations.ReplaceECPTemplateVariablesResponse](../../models/operations/replaceecptemplatevariablesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## save_portal_files

Add files to portal

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.SavePortalFile(
    files=[
        components.SavePortalFileFiles(
            file_type='orderRightTeaser',
            tags=[
                '<value>',
            ],
            filename='12345',
        ),
    ],
    origin=components.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.save_portal_files(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.SavePortalFile](../../models/components/saveportalfile.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.SavePortalFilesResponse](../../models/operations/saveportalfilesresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorResp    | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 4x-5xx              | */*                 |

## upsert_email_templates

Upserts the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_email_templates(email_templates=components.EmailTemplates(
    confirm_account='701f089d-6953-48b5-ac35-442de7c59cd3',
    forgot_password='6538fddb-f0e9-4f0f-af51-6e57891ff20a',
    invitation='14ae65fb-0dc1-4863-8743-6bc01da469f6',
    on_doc_upload='c8ee93c0-8158-4da7-82f3-114f0c7b20ff',
    on_map_a_pending_user='940134fa-50f2-4204-a08a-fd3afddbf39a',
    on_new_quote='b03e2b88-8f3f-4a93-8118-1fb07e9198a1',
), origin=components.Origin.END_CUSTOMER_PORTAL)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `email_templates`                                                      | [components.EmailTemplates](../../models/components/emailtemplates.md) | :heavy_check_mark:                                                     | Email templates payload                                                |
| `origin`                                                               | [components.Origin](../../models/components/origin.md)                 | :heavy_check_mark:                                                     | Origin of the portal                                                   |


### Response

**[operations.UpsertEmailTemplatesResponse](../../models/operations/upsertemailtemplatesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## upsert_portal

Upserts the settings for a portal of an organization.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_portal(upsert_portal_config=components.UpsertPortalConfig(
    design_id='9ba94f20-b872-4217-a259-2a90a8ee1a29',
    contact_identifiers=[
        'email',
        'last_name',
    ],
    domain='abc.com',
    name='Installer Portal',
    registration_identifiers=[
        components.RegistrationIdentifier(
            name='email',
            schema=components.EntitySlug.CONTACT,
        ),
        components.RegistrationIdentifier(
            name='last_name',
            schema=components.EntitySlug.CONTACT,
        ),
        components.RegistrationIdentifier(
            name='contract_number',
            schema=components.EntitySlug.CONTRACT,
        ),
    ],
), origin=components.Origin.INSTALLER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upsert_portal_config`                                                         | [components.UpsertPortalConfig](../../models/components/upsertportalconfig.md) | :heavy_check_mark:                                                             | Portal payload                                                                 |
| `origin`                                                                       | [components.Origin](../../models/components/origin.md)                         | :heavy_check_mark:                                                             | Origin of the portal                                                           |


### Response

**[operations.UpsertPortalResponse](../../models/operations/upsertportalresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,403,500  | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## upsert_portal_widget

Upsert widget for a portal of an organization.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.upsert_portal_widget(upsert_portal_widget=components.UpsertPortalWidget(
    widgets=[
        components.WidgetBase(
            id='<id>',
            list_index=393843,
            type=components.WidgetBaseType.CONTENT_WIDGET,
        ),
    ],
), origin=components.Origin.INSTALLER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upsert_portal_widget`                                                         | [components.UpsertPortalWidget](../../models/components/upsertportalwidget.md) | :heavy_check_mark:                                                             | Portal widgets payload                                                         |
| `origin`                                                                       | [components.Origin](../../models/components/origin.md)                         | :heavy_check_mark:                                                             | Origin of the portal                                                           |


### Response

**[operations.UpsertPortalWidgetResponse](../../models/operations/upsertportalwidgetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,403,500  | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
