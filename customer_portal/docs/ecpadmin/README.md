# ecp_admin

## Overview

APIs defined for a ECP Admin

### Available Operations

* [configure_distribution](#configure_distribution) - configureDistribution
* [create_sso_user](#create_sso_user) - createSSOUser
* [delete_portal](#delete_portal) - deletePortal
* [extra_permission_attributes](#extra_permission_attributes) - extraPermissionAttributes
* [get_all_portal_configs](#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](#get_ecp_contact) - getECPContact
* [get_email_templates](#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](#get_entity_identifiers) - getEntityIdentifiers
* [get_org_portal_config](#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_valid_secondary_attributes](#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [replace_ecp_template_variables](#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](#save_portal_files) - savePortalFiles
* [upsert_email_templates](#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](#upsert_portal) - upsertPortal

## configure_distribution

Configure the distribution for the portal's custom domain

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.ConfigureDistributionRequest(
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.configure_distribution(req, operations.ConfigureDistributionSecurity(
    epilot_auth="",
))

if res.configure_distribution_200_application_json_object is not None:
    # handle response
```

## create_sso_user

Creates a portal user as an SSO user.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.CreateSSOUserRequest(
    create_sso_user_request=shared.CreateSSOUserRequest(
        email='testemail921@yopmail.com',
        first_name='John',
        last_name='Doe',
    ),
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.create_sso_user(req, operations.CreateSSOUserSecurity(
    epilot_auth="",
))

if res.create_sso_user_201_application_json_object is not None:
    # handle response
```

## delete_portal

Deletes the portal.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.DeletePortalRequest(
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp_admin.delete_portal(req, operations.DeletePortalSecurity(
    epilot_auth="",
))

if res.status_code == 200:
    # handle response
```

## extra_permission_attributes

Retrieves the extra permission attributes.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.extra_permission_attributes(operations.ExtraPermissionAttributesSecurity(
    epilot_auth="",
))

if res.extra_permission_attributes_200_application_json_object is not None:
    # handle response
```

## get_all_portal_configs

Retrieves all portal configurations.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.get_all_portal_configs(operations.GetAllPortalConfigsSecurity(
    epilot_auth="",
))

if res.get_all_portal_configs_200_application_json_object is not None:
    # handle response
```

## get_ecp_contact

Get the Contact by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()

req = operations.GetECPContactRequest(
    id='1234',
)

res = s.ecp_admin.get_ecp_contact(req, operations.GetECPContactSecurity(
    epilot_auth="",
))

if res.get_ecp_contact_200_application_json_object is not None:
    # handle response
```

## get_email_templates

Retrieves the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetEmailTemplatesRequest(
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp_admin.get_email_templates(req, operations.GetEmailTemplatesSecurity(
    epilot_auth="",
))

if res.email_templates is not None:
    # handle response
```

## get_entity_identifiers

Retrieve a list of entity identifiers used for entity search by portal users.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetEntityIdentifiersRequest(
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp_admin.get_entity_identifiers(req, operations.GetEntityIdentifiersSecurity(
    epilot_auth="",
))

if res.get_entity_identifiers_200_application_json_object is not None:
    # handle response
```

## get_org_portal_config

Retrieves the portal configuration for the organization.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetOrgPortalConfigRequest(
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp_admin.get_org_portal_config(req, operations.GetOrgPortalConfigSecurity(
    epilot_auth="",
))

if res.portal_config is not None:
    # handle response
```

## get_portal_config

Retrieves the portal configuration.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.GetPortalConfigRequest(
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp_admin.get_portal_config(req, operations.GetPortalConfigSecurity(
    epilot_auth="",
))

if res.portal_config is not None:
    # handle response
```

## get_valid_secondary_attributes

Get valid secondary attributes that are used while mapping a contact on registration

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.ecp_admin.get_valid_secondary_attributes(operations.GetValidSecondaryAttributesSecurity(
    epilot_auth="",
))

if res.get_valid_secondary_attributes_200_application_json_object is not None:
    # handle response
```

## replace_ecp_template_variables

Replaces the template variables of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.ReplaceECPTemplateVariablesRequest(
    request_body=operations.ReplaceECPTemplateVariablesRequestBody(
        contact_id='7aa44fb8-d60e-40cc-9a3a-ba09a1ff7f51',
    ),
    origin=shared.Origin.END_CUSTOMER_PORTAL,
)

res = s.ecp_admin.replace_ecp_template_variables(req, operations.ReplaceECPTemplateVariablesSecurity(
    epilot_auth="",
))

if res.replace_ecp_template_variables_200_application_json_object is not None:
    # handle response
```

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
                'esse',
                'ipsum',
                'excepturi',
            ],
            file_type='orderRightTeaser',
            filename='12345',
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
        shared.SavePortalFileFiles(
            tags=[
                'perferendis',
            ],
            file_type='orderRightTeaser',
            filename='12345',
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
        shared.SavePortalFileFiles(
            tags=[
                'natus',
                'sed',
            ],
            file_type='orderRightTeaser',
            filename='12345',
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket='12345',
                key='12345',
            ),
        ),
        shared.SavePortalFileFiles(
            tags=[
                'dolor',
                'natus',
                'laboriosam',
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

res = s.ecp_admin.save_portal_files(req, operations.SavePortalFilesSecurity(
    epilot_auth="",
))

if res.save_portal_files_201_application_json_object is not None:
    # handle response
```

## upsert_email_templates

Upserts the email templates of a portal

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.UpsertEmailTemplatesRequest(
    email_templates=shared.EmailTemplates(
        confirm_account='701f089d-6953-48b5-ac35-442de7c59cd3',
        forgot_password='6538fddb-f0e9-4f0f-af51-6e57891ff20a',
        invitation='14ae65fb-0dc1-4863-8743-6bc01da469f6',
        on_map_a_pending_user='940134fa-50f2-4204-a08a-fd3afddbf39a',
        on_new_quote='b03e2b88-8f3f-4a93-8118-1fb07e9198a1',
    ),
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.upsert_email_templates(req, operations.UpsertEmailTemplatesSecurity(
    epilot_auth="",
))

if res.upsert_email_templates_200_application_json_object is not None:
    # handle response
```

## upsert_portal

Upserts the settings for a portal of an organization.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.UpsertPortalRequest(
    upsert_portal_config=shared.UpsertPortalConfig(
        cognito_details=shared.UpsertPortalConfigCognitoDetails(
            cognito_user_pool_arn='arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_123412341',
            cognito_user_pool_client_id='6bsd0jkgoie74k2i8mrhc1vest',
            cognito_user_pool_id='eu-central-1_CUEQRNbUb',
        ),
        config='fuga',
        contact_secondary_identifier='full_name',
        default_user_to_notify=shared.UpsertPortalConfigDefaultUserToNotify(
            on_pending_user={
                "corporis": 'iste',
                "iure": 'saepe',
            },
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
        enabled=False,
        entity_actions=[
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de='architecto',
                    en='ipsa',
                ),
                journey_id='reiciendis',
                slug=shared.EntitySlug.CONTACT,
            ),
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de='est',
                    en='mollitia',
                ),
                journey_id='laborum',
                slug=shared.EntitySlug.CONTACT,
            ),
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de='dolores',
                    en='dolorem',
                ),
                journey_id='corporis',
                slug=shared.EntitySlug.CONTACT,
            ),
        ],
        entity_identifiers=shared.UpsertPortalConfigEntityIdentifiers(
            type=shared.UpsertPortalConfigEntityIdentifiersType(
                attributes=[
                    'contract_number',
                ],
                is_enabled=False,
            ),
        ),
        grants=[
            shared.Grant(
                action='entity-read',
                effect=shared.GrantEffect.ALLOW,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                effect=shared.GrantEffect.DENY,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                effect=shared.GrantEffect.ALLOW,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
            shared.Grant(
                action='entity-read',
                effect=shared.GrantEffect.ALLOW,
                resource='entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947',
            ),
        ],
        images=shared.UpsertPortalConfigImages(
            order_left_teaser='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-left-teaser.jpeg',
            order_right_teaser='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-right-teaser.jpeg',
            welcome_banner='https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/welcome-banner.jpeg',
        ),
        is_epilot_domain=False,
        name='Installer Portal',
        self_registration=False,
    ),
    origin=shared.Origin.INSTALLER_PORTAL,
)

res = s.ecp_admin.upsert_portal(req, operations.UpsertPortalSecurity(
    epilot_auth="",
))

if res.portal_config is not None:
    # handle response
```
