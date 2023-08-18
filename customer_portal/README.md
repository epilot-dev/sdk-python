# epilot-customer-portal

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=customer_portal
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.AddEndCustomerRelationToEntityRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp.add_end_customer_relation_to_entity(req, operations.AddEndCustomerRelationToEntitySecurity(
    portal_auth="",
))

if res.add_end_customer_relation_to_entity_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [ecp](docs/sdks/ecp/README.md)

* [add_end_customer_relation_to_entity](docs/sdks/ecp/README.md#add_end_customer_relation_to_entity) - addEndCustomerRelationToEntity
* [delete_entity_file](docs/sdks/ecp/README.md#delete_entity_file) - deleteEntityFile
* [delete_portal_user](docs/sdks/ecp/README.md#delete_portal_user) - deletePortalUser
* [get_all_contracts](docs/sdks/ecp/README.md#get_all_contracts) - getAllContracts
* [get_all_files](docs/sdks/ecp/README.md#get_all_files) - getAllFiles
* [get_all_opportunities](docs/sdks/ecp/README.md#get_all_opportunities) - getAllOpportunities
* [get_all_orders](docs/sdks/ecp/README.md#get_all_orders) - getAllOrders
* [get_contact](docs/sdks/ecp/README.md#get_contact) - getContact
* [get_contract](docs/sdks/ecp/README.md#get_contract) - getContract
* [get_entities_by_identifiers](docs/sdks/ecp/README.md#get_entities_by_identifiers) - getEntitiesByIdentifiers
* [get_file_by_id](docs/sdks/ecp/README.md#get_file_by_id) - getFileById
* [get_files_count_by_entity](docs/sdks/ecp/README.md#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](docs/sdks/ecp/README.md#get_opportunity) - getOpportunity
* [get_order](docs/sdks/ecp/README.md#get_order) - getOrder
* [get_organization_settings](docs/sdks/ecp/README.md#get_organization_settings) - getOrganizationSettings
* [get_portal_config](docs/sdks/ecp/README.md#get_portal_config) - getPortalConfig
* [get_portal_user](docs/sdks/ecp/README.md#get_portal_user) - getPortalUser
* [get_portal_widgets](docs/sdks/ecp/README.md#get_portal_widgets) - getPortalWidgets
* [get_schemas](docs/sdks/ecp/README.md#get_schemas) - getSchemas
* [save_entity_file](docs/sdks/ecp/README.md#save_entity_file) - saveEntityFile
* [update_contact](docs/sdks/ecp/README.md#update_contact) - updateContact
* [update_contract](docs/sdks/ecp/README.md#update_contract) - updateContract
* [update_opportunity](docs/sdks/ecp/README.md#update_opportunity) - updateOpportunity
* [update_order](docs/sdks/ecp/README.md#update_order) - updateOrder
* [update_portal_user](docs/sdks/ecp/README.md#update_portal_user) - updatePortalUser

### [ecp_admin](docs/sdks/ecpadmin/README.md)

* [configure_distribution](docs/sdks/ecpadmin/README.md#configure_distribution) - configureDistribution
* [create_sso_user](docs/sdks/ecpadmin/README.md#create_sso_user) - createSSOUser
* [delete_portal](docs/sdks/ecpadmin/README.md#delete_portal) - deletePortal
* [extra_permission_attributes](docs/sdks/ecpadmin/README.md#extra_permission_attributes) - extraPermissionAttributes
* [get_all_portal_configs](docs/sdks/ecpadmin/README.md#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](docs/sdks/ecpadmin/README.md#get_ecp_contact) - getECPContact
* [get_email_templates](docs/sdks/ecpadmin/README.md#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](docs/sdks/ecpadmin/README.md#get_entity_identifiers) - getEntityIdentifiers
* [get_org_portal_config](docs/sdks/ecpadmin/README.md#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](docs/sdks/ecpadmin/README.md#get_portal_config) - getPortalConfig
* [get_portal_widgets](docs/sdks/ecpadmin/README.md#get_portal_widgets) - getPortalWidgets
* [get_valid_secondary_attributes](docs/sdks/ecpadmin/README.md#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [replace_ecp_template_variables](docs/sdks/ecpadmin/README.md#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](docs/sdks/ecpadmin/README.md#save_portal_files) - savePortalFiles
* [upsert_email_templates](docs/sdks/ecpadmin/README.md#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](docs/sdks/ecpadmin/README.md#upsert_portal) - upsertPortal
* [upsert_portal_widget](docs/sdks/ecpadmin/README.md#upsert_portal_widget) - upsertPortalWidget

### [public](docs/sdks/public/README.md)

* [confirm_user](docs/sdks/public/README.md#confirm_user) - confirmUser
* [create_user](docs/sdks/public/README.md#create_user) - createUser
* [get_contact_count](docs/sdks/public/README.md#get_contact_count) - getContactCount
* [get_count_by_email](docs/sdks/public/README.md#get_count_by_email) - getCountByEmail
* [get_portal_config_by_domain](docs/sdks/public/README.md#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](docs/sdks/public/README.md#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_widgets](docs/sdks/public/README.md#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](docs/sdks/public/README.md#user_exists) - userExists
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
