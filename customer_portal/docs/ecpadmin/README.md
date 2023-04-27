# ecp_admin

## Overview

ECP Admin

### Available Operations

* [configure_distribution](#configure_distribution) - configureDistribution
* [create_sso_user](#create_sso_user) - creates a sso user
* [delete_portal](#delete_portal) - deletePortal
* [extra_permission_attributes](#extra_permission_attributes) - extraPermissionAttributes
* [get_all_portal_configs](#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](#get_ecp_contact) - getECPContact
* [get_email_templates](#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](#get_entity_identifiers) - getEntityIdentifiers
* [get_org_portal_config](#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](#get_portal_config) - getPortalConfig
* [get_public_portal_config](#get_public_portal_config) - getPublicPortalConfig
* [get_valid_secondary_attributes](#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [replace_ecp_template_variables](#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](#save_portal_files) - Add files to portal
* [upsert_email_templates](#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](#upsert_portal) - upserts a portal

## configure_distribution

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.ConfigureDistributionRequest(
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.configure_distribution(req, operations.ConfigureDistributionSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.configure_distribution_200_application_json_object is not None:
    # handle response
```

## create_sso_user

Creates a sso user as portal user

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.CreateSSOUserRequest(
    request_body=operations.CreateSSOUserRequestBody(
        email="testemail921@yopmail.com",
        first_name="John",
        last_name="Doe",
    ),
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.create_sso_user(req, operations.CreateSSOUserSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.create_sso_user_201_application_json_object is not None:
    # handle response
```

## delete_portal

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.DeletePortalRequest(
    origin="END_CUSTOMER_PORTAL",
)

res = s.ecp_admin.delete_portal(req, operations.DeletePortalSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## extra_permission_attributes

TODO

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)


res = s.ecp_admin.extra_permission_attributes()

if res.extra_permission_attributes_200_application_json_object is not None:
    # handle response
```

## get_all_portal_configs

TODO

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)


res = s.ecp_admin.get_all_portal_configs()

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
    id="1234",
)

res = s.ecp_admin.get_ecp_contact(req, operations.GetECPContactSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
    # handle response
```

## get_email_templates

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.GetEmailTemplatesRequest(
    origin="END_CUSTOMER_PORTAL",
)

res = s.ecp_admin.get_email_templates(req, operations.GetEmailTemplatesSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.email_templates is not None:
    # handle response
```

## get_entity_identifiers

Get Entity's Identifiers

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


req = operations.GetEntityIdentifiersRequest(
    slug="contact",
)

res = s.ecp_admin.get_entity_identifiers(req, operations.GetEntityIdentifiersSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.get_entity_identifiers_200_application_json_object is not None:
    # handle response
```

## get_org_portal_config

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.GetOrgPortalConfigRequest(
    origin="END_CUSTOMER_PORTAL",
)

res = s.ecp_admin.get_org_portal_config(req, operations.GetOrgPortalConfigSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.portal_config is not None:
    # handle response
```

## get_portal_config

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.GetPortalConfigRequest(
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.get_portal_config(req, operations.GetPortalConfigSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.portal_config is not None:
    # handle response
```

## get_public_portal_config

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPublicPortalConfigRequest(
    org_id="12324",
    origin="END_CUSTOMER_PORTAL",
)

res = s.ecp_admin.get_public_portal_config(req)

if res.portal_config is not None:
    # handle response
```

## get_valid_secondary_attributes

Get Valid Secondary Attributes

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        as_customer="YOUR_API_KEY_HERE",
    ),
)


res = s.ecp_admin.get_valid_secondary_attributes()

if res.get_valid_secondary_attributes_200_application_json_object is not None:
    # handle response
```

## replace_ecp_template_variables

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.ReplaceECPTemplateVariablesRequest(
    request_body=operations.ReplaceECPTemplateVariablesRequestBody(
        contact_id="7aa44fb8-d60e-40cc-9a3a-ba09a1ff7f51",
    ),
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.replace_ecp_template_variables(req, operations.ReplaceECPTemplateVariablesSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
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
                "12345",
                "12345",
                "12345",
                "12345",
            ],
            file_type="orderRightTeaser",
            filename="12345",
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket="12345",
                key="12345",
            ),
        ),
        shared.SavePortalFileFiles(
            tags=[
                "12345",
                "12345",
                "12345",
                "12345",
            ],
            file_type="orderRightTeaser",
            filename="12345",
            s3ref=shared.SavePortalFileFilesS3ref(
                bucket="12345",
                key="12345",
            ),
        ),
    ],
    origin="END_CUSTOMER_PORTAL",
)

res = s.ecp_admin.save_portal_files(req, operations.SavePortalFilesSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.entity_item is not None:
    # handle response
```

## upsert_email_templates

TODO

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.UpsertEmailTemplatesRequest(
    email_templates=shared.EmailTemplates(
        confirm_account="saepe",
        forgot_password="pariatur",
        invitation="accusantium",
        on_map_a_pending_user="consequuntur",
        on_new_quote="praesentium",
    ),
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.upsert_email_templates(req, operations.UpsertEmailTemplatesSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.upsert_email_templates_200_application_json_object is not None:
    # handle response
```

## upsert_portal

upserts a portal and db item

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = operations.UpsertPortalRequest(
    upsert_portal_config=shared.UpsertPortalConfig(
        cognito_details=shared.UpsertPortalConfigCognitoDetails(
            cognito_user_pool_arn="arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_123412341",
            cognito_user_pool_client_id="6bsd0jkgoie74k2i8mrhc1vest",
            cognito_user_pool_id="eu-central-1_CUEQRNbUb",
        ),
        config="magni",
        contact_secondary_identifier="full_name",
        default_user_to_notify={
            "quo": "illum",
        },
        design_id="3134",
        email_templates=shared.UpsertPortalConfigEmailTemplates(
            confirm_account="701f089d-6953-48b5-ac35-442de7c59cd3",
            forgot_password="6538fddb-f0e9-4f0f-af51-6e57891ff20a",
            invitation="14ae65fb-0dc1-4863-8743-6bc01da469f6",
        ),
        enabled=True,
        entity_actions=[
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de="maxime",
                    en="ea",
                ),
                journey_id="excepturi",
                slug="contact",
            ),
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de="odit",
                    en="ea",
                ),
                journey_id="accusantium",
                slug="contact",
            ),
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de="ab",
                    en="maiores",
                ),
                journey_id="quidem",
                slug="contact",
            ),
            shared.UpsertPortalConfigEntityActions(
                action_label=shared.UpsertPortalConfigEntityActionsActionLabel(
                    de="ipsam",
                    en="voluptate",
                ),
                journey_id="autem",
                slug="contact",
            ),
        ],
        entity_identifiers={
            "eaque": shared.UpsertPortalConfigEntityIdentifiers(
                attributes=[
                    "contract_number",
                    "contract_number",
                    "contract_number",
                    "contract_number",
                ],
                is_enabled=False,
            ),
            "nemo": shared.UpsertPortalConfigEntityIdentifiers(
                attributes=[
                    "contract_number",
                    "contract_number",
                    "contract_number",
                    "contract_number",
                ],
                is_enabled=False,
            ),
            "perferendis": shared.UpsertPortalConfigEntityIdentifiers(
                attributes=[
                    "contract_number",
                    "contract_number",
                    "contract_number",
                    "contract_number",
                ],
                is_enabled=False,
            ),
        },
        grants=[
            shared.Grant(
                action="entity-read",
                effect="allow",
                resource="entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947",
            ),
        ],
        images=shared.UpsertPortalConfigImages(
            order_left_teaser="https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-left-teaser.jpeg",
            order_right_teaser="https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/order-right-teaser.jpeg",
            welcome_banner="https://epilot-bucket.s3.eu-central-1.amazonaws.com/12344/6538fddb-f0e9-4f0f-af51-6e57891ff20a/welcome-banner.jpeg",
        ),
        is_epilot_domain=True,
        name="My Portal",
        self_registration=False,
    ),
    origin="INSTALLER_PORTAL",
)

res = s.ecp_admin.upsert_portal(req, operations.UpsertPortalSecurity(
    epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.add_portal_resp is not None:
    # handle response
```
