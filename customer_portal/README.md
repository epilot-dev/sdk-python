# epilot-customer-portal

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=customer_portal
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=customer_portal
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_customer_portal
from epilot_customer_portal import Epilot

async def main():
    async with Epilot(
        security=epilot_customer_portal.Security(
            either_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:

        res = await epilot.ecp_admin.can_trigger_portal_flow_async(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, activity_id="01F130Q52Q6MWSNS8N2AVXV4JN", ecp_config={
            "file_config": {
                "tags": [
                    "example",
                    "mock",
                ],
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [activity](docs/sdks/activity/README.md)

* [get_entity_activity_feed](docs/sdks/activity/README.md#get_entity_activity_feed) - getEntityActivityFeed

### [balance](docs/sdks/balancesdk/README.md)

* [get_customer_balance](docs/sdks/balancesdk/README.md#get_customer_balance) - getCustomerBalance

### [ecp](docs/sdks/ecp/README.md)

* [add_contract_by_identifiers](docs/sdks/ecp/README.md#add_contract_by_identifiers) - addContractByIdentifiers
* [create_custom_entity_activity](docs/sdks/ecp/README.md#create_custom_entity_activity) - createCustomEntityActivity
* [create_meter_reading](docs/sdks/ecp/README.md#create_meter_reading) - Create Meter Reading
* [delete_entity_file](docs/sdks/ecp/README.md#delete_entity_file) - deleteEntityFile
* [delete_portal_user](docs/sdks/ecp/README.md#delete_portal_user) - deletePortalUser
* [get_all_contracts](docs/sdks/ecp/README.md#get_all_contracts) - getAllContracts
* [get_all_files](docs/sdks/ecp/README.md#get_all_files) - getAllFiles
* [get_all_opportunities](docs/sdks/ecp/README.md#get_all_opportunities) - getAllOpportunities
* [get_all_orders](docs/sdks/ecp/README.md#get_all_orders) - getAllOrders
* [get_billing_events](docs/sdks/ecp/README.md#get_billing_events) - getBillingEvents
* [get_consumption](docs/sdks/ecp/README.md#get_consumption) - Get Consumption
* [get_contact](docs/sdks/ecp/README.md#get_contact) - getContact
* [get_contract](docs/sdks/ecp/README.md#get_contract) - getContract
* [get_costs](docs/sdks/ecp/README.md#get_costs) - Get Costs
* [get_external_links](docs/sdks/ecp/README.md#get_external_links) - getExternalLinks
* [get_file_by_id](docs/sdks/ecp/README.md#get_file_by_id) - getFileById
* [get_files_count_by_entity](docs/sdks/ecp/README.md#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](docs/sdks/ecp/README.md#get_opportunity) - getOpportunity
* [get_order](docs/sdks/ecp/README.md#get_order) - getOrder
* [get_organization_settings](docs/sdks/ecp/README.md#get_organization_settings) - getOrganizationSettings
* [get_portal_config](docs/sdks/ecp/README.md#get_portal_config) - getPortalConfig
* [get_portal_user](docs/sdks/ecp/README.md#get_portal_user) - getPortalUser
* [get_portal_widgets](docs/sdks/ecp/README.md#get_portal_widgets) - getPortalWidgets
* [get_prices](docs/sdks/ecp/README.md#get_prices) - Get Prices
* [get_resolved_external_link](docs/sdks/ecp/README.md#get_resolved_external_link) - getResolvedExternalLink
* [get_schemas](docs/sdks/ecp/README.md#get_schemas) - getSchemas
* [get_search_results_for_opportunities](docs/sdks/ecp/README.md#get_search_results_for_opportunities) - getSearchResultsForOpportunities
* [get_searchable_attributes_for_opportunities](docs/sdks/ecp/README.md#get_searchable_attributes_for_opportunities) - getSearchableAttributesForOpportunities
* [post_order_acceptance](docs/sdks/ecp/README.md#post_order_acceptance) - postOrderAcceptance
* [revoke_token](docs/sdks/ecp/README.md#revoke_token) - revokeToken
* [save_entity_file](docs/sdks/ecp/README.md#save_entity_file) - saveEntityFile
* [search_payment_relations_in_entities](docs/sdks/ecp/README.md#search_payment_relations_in_entities) - searchPaymentRelationsInEntities
* [search_portal_user_entities](docs/sdks/ecp/README.md#search_portal_user_entities) - searchPortalUserEntities
* [track_file_downloaded](docs/sdks/ecp/README.md#track_file_downloaded) - trackFileDownloaded
* [trigger_entity_access_event](docs/sdks/ecp/README.md#trigger_entity_access_event) - triggerEntityAccessEvent
* [update_contact](docs/sdks/ecp/README.md#update_contact) - updateContact
* [update_contract](docs/sdks/ecp/README.md#update_contract) - updateContract
* [update_opportunity](docs/sdks/ecp/README.md#update_opportunity) - updateOpportunity
* [update_order](docs/sdks/ecp/README.md#update_order) - updateOrder
* [update_portal_user](docs/sdks/ecp/README.md#update_portal_user) - updatePortalUser
* [update_portal_user_email](docs/sdks/ecp/README.md#update_portal_user_email) - updatePortalUserEmail
* [update_workflow_step_as_done](docs/sdks/ecp/README.md#update_workflow_step_as_done) - updateWorkflowStepAsDone
* [validate_cadence_entity_edit_rules](docs/sdks/ecp/README.md#validate_cadence_entity_edit_rules) - validateCadenceEntityEditRules
* [validate_token](docs/sdks/ecp/README.md#validate_token) - validateToken

### [ecp_admin](docs/sdks/ecpadmin/README.md)

* [can_trigger_portal_flow](docs/sdks/ecpadmin/README.md#can_trigger_portal_flow) - canTriggerPortalFlow
* [configure_distribution](docs/sdks/ecpadmin/README.md#configure_distribution) - configureDistribution
* [create_sso_user](docs/sdks/ecpadmin/README.md#create_sso_user) - createSSOUser
* [delete_portal](docs/sdks/ecpadmin/README.md#delete_portal) - deletePortal
* [extra_permission_attributes](docs/sdks/ecpadmin/README.md#extra_permission_attributes) - extraPermissionAttributes
* [fetch_portal_users_by_related_entity](docs/sdks/ecpadmin/README.md#fetch_portal_users_by_related_entity) - fetchPortalUsersByRelatedEntity
* [get_all_portal_configs](docs/sdks/ecpadmin/README.md#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](docs/sdks/ecpadmin/README.md#get_ecp_contact) - getECPContact
* [get_email_templates](docs/sdks/ecpadmin/README.md#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](docs/sdks/ecpadmin/README.md#get_entity_identifiers) - getEntityIdentifiers
* [get_external_links](docs/sdks/ecpadmin/README.md#get_external_links) - getExternalLinks
* [get_org_portal_config](docs/sdks/ecpadmin/README.md#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](docs/sdks/ecpadmin/README.md#get_portal_config) - getPortalConfig
* [get_portal_extensions](docs/sdks/ecpadmin/README.md#get_portal_extensions) - getPortalExtensions
* [get_portal_widgets](docs/sdks/ecpadmin/README.md#get_portal_widgets) - getPortalWidgets
* [get_recipients_to_notify_on_automation](docs/sdks/ecpadmin/README.md#get_recipients_to_notify_on_automation) - getRecipientsToNotifyOnAutomation
* [get_registration_identifiers](docs/sdks/ecpadmin/README.md#get_registration_identifiers) - getRegistrationIdentifiers
* [get_resolved_external_link](docs/sdks/ecpadmin/README.md#get_resolved_external_link) - getResolvedExternalLink
* [get_valid_secondary_attributes](docs/sdks/ecpadmin/README.md#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](docs/sdks/ecpadmin/README.md#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](docs/sdks/ecpadmin/README.md#replace_ecp_template_variables) - replaceECPTemplateVariables
* [resend_confirmation_email](docs/sdks/ecpadmin/README.md#resend_confirmation_email) - resendConfirmationEmail
* [save_portal_files](docs/sdks/ecpadmin/README.md#save_portal_files) - savePortalFiles
* [upsert_email_templates](docs/sdks/ecpadmin/README.md#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](docs/sdks/ecpadmin/README.md#upsert_portal) - upsertPortal
* [upsert_portal_widget](docs/sdks/ecpadmin/README.md#upsert_portal_widget) - upsertPortalWidget


### [public](docs/sdks/public/README.md)

* [check_contact_exists](docs/sdks/public/README.md#check_contact_exists) - checkContactExists
* [confirm_user](docs/sdks/public/README.md#confirm_user) - confirmUser
* [confirm_user_with_user_id](docs/sdks/public/README.md#confirm_user_with_user_id) - confirmUserWithUserId
* [create_user](docs/sdks/public/README.md#create_user) - createUser
* [get_portal_config_by_domain](docs/sdks/public/README.md#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](docs/sdks/public/README.md#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_extension_details](docs/sdks/public/README.md#get_public_portal_extension_details) - getPublicPortalExtensionDetails
* [get_public_portal_widgets](docs/sdks/public/README.md#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](docs/sdks/public/README.md#user_exists) - userExists

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
