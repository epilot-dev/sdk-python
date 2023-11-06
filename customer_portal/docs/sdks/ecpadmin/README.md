# ECPAdmin
(*ecp_admin*)

## Overview

APIs defined for a ECP Admin

### Available Operations

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
* [get_valid_secondary_attributes](#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](#save_portal_files) - savePortalFiles
* [upsert_email_templates](#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](#upsert_portal) - upsertPortal
* [upsert_portal_widget](#upsert_portal_widget) - upsertPortalWidget

## configure_distribution

Configure the distribution for the portal's custom domain

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.configure_distribution("", origin=shared.Origin.INSTALLER_PORTAL)

if res.configure_distribution_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.ConfigureDistributionSecurity](../../models/operations/configuredistributionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `origin`                                                                                             | [shared.Origin](../../models/shared/origin.md)                                                       | :heavy_check_mark:                                                                                   | Origin of the portal                                                                                 |


### Response

**[operations.ConfigureDistributionResponse](../../models/operations/configuredistributionresponse.md)**


## create_sso_user

Creates a portal user as an SSO user.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.create_sso_user("", create_sso_user_request=shared.CreateSSOUserRequest(
    email='testemail921@yopmail.com',
    first_name='John',
    last_name='Doe',
), origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.create_sso_user_201_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.CreateSSOUserSecurity](../../models/operations/createssousersecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `create_sso_user_request`                                                            | [shared.CreateSSOUserRequest](../../models/shared/createssouserrequest.md)           | :heavy_check_mark:                                                                   | Portal user payload                                                                  |
| `origin`                                                                             | [shared.Origin](../../models/shared/origin.md)                                       | :heavy_check_mark:                                                                   | Origin of the portal                                                                 |


### Response

**[operations.CreateSSOUserResponse](../../models/operations/createssouserresponse.md)**


## delete_portal

Deletes the portal.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.delete_portal("", origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.DeletePortalSecurity](../../models/operations/deleteportalsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |
| `origin`                                                                           | [shared.Origin](../../models/shared/origin.md)                                     | :heavy_check_mark:                                                                 | Origin of the portal                                                               |


### Response

**[operations.DeletePortalResponse](../../models/operations/deleteportalresponse.md)**


## extra_permission_attributes

Retrieves the extra permission attributes.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.extra_permission_attributes("")

if res.extra_permission_attributes_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                   | [operations.ExtraPermissionAttributesSecurity](../../models/operations/extrapermissionattributessecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.ExtraPermissionAttributesResponse](../../models/operations/extrapermissionattributesresponse.md)**


## fetch_portal_users_by_related_entity

Get all users for a given entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.fetch_portal_users_by_related_entity("", entity_id='5da0a718-c822-403d-9f5d-20d4584e0528', slug=shared.EntitySlug.CONTACT)

if res.fetch_portal_users_by_related_entity_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                               | [operations.FetchPortalUsersByRelatedEntitySecurity](../../models/operations/fetchportalusersbyrelatedentitysecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |                                                                                                                          |
| `entity_id`                                                                                                              | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      | 5da0a718-c822-403d-9f5d-20d4584e0528                                                                                     |
| `slug`                                                                                                                   | [shared.EntitySlug](../../models/shared/entityslug.md)                                                                   | :heavy_check_mark:                                                                                                       | URL-friendly identifier for the entity schema                                                                            | contact                                                                                                                  |


### Response

**[operations.FetchPortalUsersByRelatedEntityResponse](../../models/operations/fetchportalusersbyrelatedentityresponse.md)**


## get_all_portal_configs

Retrieves all portal configurations.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.get_all_portal_configs("")

if res.get_all_portal_configs_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetAllPortalConfigsSecurity](../../models/operations/getallportalconfigssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAllPortalConfigsResponse](../../models/operations/getallportalconfigsresponse.md)**


## get_ecp_contact

Get the Contact by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.get_ecp_contact("", id='1234')

if res.get_ecp_contact_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.GetECPContactSecurity](../../models/operations/getecpcontactsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |                                                                                      |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  | 1234                                                                                 |


### Response

**[operations.GetECPContactResponse](../../models/operations/getecpcontactresponse.md)**


## get_email_templates

Retrieves the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.get_email_templates("", origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.email_templates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.GetEmailTemplatesSecurity](../../models/operations/getemailtemplatessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `origin`                                                                                     | [shared.Origin](../../models/shared/origin.md)                                               | :heavy_check_mark:                                                                           | Origin of the portal                                                                         |


### Response

**[operations.GetEmailTemplatesResponse](../../models/operations/getemailtemplatesresponse.md)**


## get_entity_identifiers

Retrieve a list of entity identifiers used for entity search by portal users.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.get_entity_identifiers("", slug=shared.EntitySlug.CONTACT)

if res.get_entity_identifiers_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.GetEntityIdentifiersSecurity](../../models/operations/getentityidentifierssecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |                                                                                                    |
| `slug`                                                                                             | [shared.EntitySlug](../../models/shared/entityslug.md)                                             | :heavy_check_mark:                                                                                 | The slug of an entity                                                                              | contact                                                                                            |


### Response

**[operations.GetEntityIdentifiersResponse](../../models/operations/getentityidentifiersresponse.md)**


## get_org_portal_config

Retrieves the portal configuration for the organization.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.get_org_portal_config("", origin=shared.Origin.INSTALLER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `security`                                                                                     | [operations.GetOrgPortalConfigSecurity](../../models/operations/getorgportalconfigsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `origin`                                                                                       | [shared.Origin](../../models/shared/origin.md)                                                 | :heavy_check_mark:                                                                             | Origin of the portal                                                                           |


### Response

**[operations.GetOrgPortalConfigResponse](../../models/operations/getorgportalconfigresponse.md)**


## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.get_portal_config(operations.GetPortalConfigSecurity(
    epilot_auth="",
), origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.GetPortalConfigSecurity](../../models/operations/getportalconfigsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `origin`                                                                                 | [Optional[shared.Origin]](../../models/shared/origin.md)                                 | :heavy_minus_sign:                                                                       | Origin of the portal                                                                     |


### Response

**[operations.GetPortalConfigResponse](../../models/operations/getportalconfigresponse.md)**


## get_portal_widgets

Retrieves the widgets of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.get_portal_widgets(operations.GetPortalWidgetsSecurity(
    epilot_auth="",
), origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.GetPortalWidgetsSecurity](../../models/operations/getportalwidgetssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `origin`                                                                                   | [Optional[shared.Origin]](../../models/shared/origin.md)                                   | :heavy_minus_sign:                                                                         | Origin of the portal                                                                       |


### Response

**[operations.GetPortalWidgetsResponse](../../models/operations/getportalwidgetsresponse.md)**


## get_valid_secondary_attributes

Get valid secondary attributes that are used while mapping a contact on registration

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.get_valid_secondary_attributes("")

if res.get_valid_secondary_attributes_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                       | [operations.GetValidSecondaryAttributesSecurity](../../models/operations/getvalidsecondaryattributessecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetValidSecondaryAttributesResponse](../../models/operations/getvalidsecondaryattributesresponse.md)**


## login_to_portal_as_user

Generate a token to log in to a portal impersonating a users.

Token is valid for 5 minutes.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.LoginToPortalAsUserRequestBody(
    email='portal-customer@email.com',
)

res = s.ecp_admin.login_to_portal_as_user(req, "")

if res.login_to_portal_as_user_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.LoginToPortalAsUserRequestBody](../../models/operations/logintoportalasuserrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.LoginToPortalAsUserSecurity](../../models/operations/logintoportalasusersecurity.md)       | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.LoginToPortalAsUserResponse](../../models/operations/logintoportalasuserresponse.md)**


## replace_ecp_template_variables

Replaces the template variables of a portal

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.ReplaceECPTemplateVariablesRequestBody(
    contact_id='7aa44fb8-d60e-40cc-9a3a-ba09a1ff7f51',
)

res = s.ecp_admin.replace_ecp_template_variables(req, "")

if res.replace_ecp_template_variables_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.ReplaceECPTemplateVariablesRequestBody](../../models/operations/replaceecptemplatevariablesrequestbody.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.ReplaceECPTemplateVariablesSecurity](../../models/operations/replaceecptemplatevariablessecurity.md)       | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.ReplaceECPTemplateVariablesResponse](../../models/operations/replaceecptemplatevariablesresponse.md)**


## save_portal_files

Add files to portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = shared.SavePortalFile(
    files=[
        shared.SavePortalFileFiles(
            tags=[
                'string',
            ],
            file_type='orderRightTeaser',
            filename='12345',
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
    ],
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.save_portal_files(req, "")

if res.save_portal_files_201_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.SavePortalFile](../../models/shared/saveportalfile.md)                           | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.SavePortalFilesSecurity](../../models/operations/saveportalfilessecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.SavePortalFilesResponse](../../models/operations/saveportalfilesresponse.md)**


## upsert_email_templates

Upserts the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.upsert_email_templates("", email_templates=shared.EmailTemplates(
    confirm_account='701f089d-6953-48b5-ac35-442de7c59cd3',
    forgot_password='6538fddb-f0e9-4f0f-af51-6e57891ff20a',
    invitation='14ae65fb-0dc1-4863-8743-6bc01da469f6',
    on_map_a_pending_user='940134fa-50f2-4204-a08a-fd3afddbf39a',
    on_new_quote='b03e2b88-8f3f-4a93-8118-1fb07e9198a1',
), origin=shared.Origin.END_CUSTOMER_PORTAL)

if res.upsert_email_templates_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.UpsertEmailTemplatesSecurity](../../models/operations/upsertemailtemplatessecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |
| `email_templates`                                                                                  | [shared.EmailTemplates](../../models/shared/emailtemplates.md)                                     | :heavy_check_mark:                                                                                 | Email templates payload                                                                            |
| `origin`                                                                                           | [shared.Origin](../../models/shared/origin.md)                                                     | :heavy_check_mark:                                                                                 | Origin of the portal                                                                               |


### Response

**[operations.UpsertEmailTemplatesResponse](../../models/operations/upsertemailtemplatesresponse.md)**


## upsert_portal

Upserts the settings for a portal of an organization.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.upsert_portal("", upsert_portal_config=shared.UpsertPortalConfig(
    cognito_details=shared.UpsertPortalConfigCognitoDetails(
        cognito_user_pool_arn='arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_123412341',
        cognito_user_pool_client_id='6bsd0jkgoie74k2i8mrhc1vest',
        cognito_user_pool_id='eu-central-1_CUEQRNbUb',
    ),
    contact_identifiers=[
        'email',
        'last_name',
    ],
    contact_secondary_identifier='full_name',
    default_user_to_notify=shared.UpsertPortalConfigDefaultUserToNotify(
        on_pending_user=[
            shared.AdminUser(
                additional_properties={
                    "key": 'string',
                },
                display_name='John',
                email='j.doe@epilot.cloud',
                image_uri=shared.AdminUserImageURI(
                    key='fuafjvoHKsudhfagweucjasdvga',
                    original='https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original',
                    thumbnail_32='https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original?w=32&h=32',
                    thumbnail_64='https://fuafjvoHKsu.cloudimg.io/v7/e-mage-sam-bucket-dev.s3.eu-central-1.amazonaws.com/files/fuafjvoHKsudhfagweucjasdvga/original?w=64&h=64',
                ),
                org_id='123',
                phone='12345 67890',
                type='user',
                user_id='123456',
            ),
        ],
    ),
    design_id='9ba94f20-b872-4217-a259-2a90a8ee1a29',
    domain='abc.com',
    email_templates=shared.EmailTemplates(
        confirm_account='701f089d-6953-48b5-ac35-442de7c59cd3',
        forgot_password='6538fddb-f0e9-4f0f-af51-6e57891ff20a',
        invitation='14ae65fb-0dc1-4863-8743-6bc01da469f6',
        on_map_a_pending_user='940134fa-50f2-4204-a08a-fd3afddbf39a',
        on_new_quote='b03e2b88-8f3f-4a93-8118-1fb07e9198a1',
    ),
    entity_actions=[
        shared.UpsertPortalConfigEntityActions(
            action_label=shared.UpsertPortalConfigEntityActionsActionLabel(),
            slug=shared.EntitySlug.CONTACT,
        ),
    ],
    entity_edit_rules=[
        shared.UpsertPortalConfigEntityEditRules(
            allowed_decrement='10%',
            allowed_increment='10%',
            attribute='first_name',
            cadence_period=1,
            changes_allowed=1,
            grace_period=1,
            number_of_days_before_restriction=10,
            slug=shared.EntitySlug.CONTACT,
        ),
    ],
    entity_identifiers=shared.UpsertPortalConfigEntityIdentifiers(
        type=shared.UpsertPortalConfigEntityIdentifiersType(
            attributes=[
                'c',
                'o',
                'n',
                't',
                'r',
                'a',
                'c',
                't',
                '_',
                'n',
                'u',
                'm',
                'b',
                'e',
                'r',
            ],
        ),
    ),
    feature_settings=shared.UpsertPortalConfigFeatureSettings(),
    grants=[
        shared.Grant(
            action='entity-read',
            resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
        ),
    ],
    images=shared.UpsertPortalConfigImages(
        order_left_teaser='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-left-teaser.jpeg',
        order_right_teaser='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-right-teaser.jpeg',
        welcome_banner='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/welcome-banner.jpeg',
    ),
    name='Installer Portal',
    self_registration=False,
), origin=shared.Origin.INSTALLER_PORTAL)

if res.portal_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.UpsertPortalSecurity](../../models/operations/upsertportalsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |
| `upsert_portal_config`                                                             | [shared.UpsertPortalConfig](../../models/shared/upsertportalconfig.md)             | :heavy_check_mark:                                                                 | Portal payload                                                                     |
| `origin`                                                                           | [shared.Origin](../../models/shared/origin.md)                                     | :heavy_check_mark:                                                                 | Origin of the portal                                                               |


### Response

**[operations.UpsertPortalResponse](../../models/operations/upsertportalresponse.md)**


## upsert_portal_widget

Upsert widget for a portal of an organization.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


res = s.ecp_admin.upsert_portal_widget("", upsert_portal_widget=shared.UpsertPortalWidget(
    widgets=[
        shared.WidgetBase(
            headline=shared.WidgetBaseHeadline(),
            id='<ID>',
            list_index=393843,
            sub_headline=shared.WidgetBaseSubHeadline(),
            type=shared.WidgetBaseType.ACTION_WIDGET,
        ),
    ],
), origin=shared.Origin.INSTALLER_PORTAL)

if res.upsert_portal_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `security`                                                                                     | [operations.UpsertPortalWidgetSecurity](../../models/operations/upsertportalwidgetsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `upsert_portal_widget`                                                                         | [shared.UpsertPortalWidget](../../models/shared/upsertportalwidget.md)                         | :heavy_check_mark:                                                                             | Portal widgets payload                                                                         |
| `origin`                                                                                       | [shared.Origin](../../models/shared/origin.md)                                                 | :heavy_check_mark:                                                                             | Origin of the portal                                                                           |


### Response

**[operations.UpsertPortalWidgetResponse](../../models/operations/upsertportalwidgetresponse.md)**

