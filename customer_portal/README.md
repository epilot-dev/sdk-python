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
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [.ecp_admin](docs/sdks/ecpadmin/README.md)

* [configure_distribution](docs/sdks/ecpadmin/README.md#configure_distribution) - configureDistribution
* [create_sso_user](docs/sdks/ecpadmin/README.md#create_sso_user) - createSSOUser
* [delete_portal](docs/sdks/ecpadmin/README.md#delete_portal) - deletePortal
* [extra_permission_attributes](docs/sdks/ecpadmin/README.md#extra_permission_attributes) - extraPermissionAttributes
* [fetch_portal_users_by_related_entity](docs/sdks/ecpadmin/README.md#fetch_portal_users_by_related_entity) - fetchPortalUsersByRelatedEntity
* [get_all_portal_configs](docs/sdks/ecpadmin/README.md#get_all_portal_configs) - getAllPortalConfigs
* [get_ecp_contact](docs/sdks/ecpadmin/README.md#get_ecp_contact) - getECPContact
* [get_email_templates](docs/sdks/ecpadmin/README.md#get_email_templates) - getEmailTemplates
* [get_entity_identifiers](docs/sdks/ecpadmin/README.md#get_entity_identifiers) - getEntityIdentifiers
* [get_org_portal_config](docs/sdks/ecpadmin/README.md#get_org_portal_config) - getOrgPortalConfig
* [get_portal_config](docs/sdks/ecpadmin/README.md#get_portal_config) - getPortalConfig
* [get_portal_widgets](docs/sdks/ecpadmin/README.md#get_portal_widgets) - getPortalWidgets
* [get_valid_secondary_attributes](docs/sdks/ecpadmin/README.md#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](docs/sdks/ecpadmin/README.md#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](docs/sdks/ecpadmin/README.md#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](docs/sdks/ecpadmin/README.md#save_portal_files) - savePortalFiles
* [upsert_email_templates](docs/sdks/ecpadmin/README.md#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](docs/sdks/ecpadmin/README.md#upsert_portal) - upsertPortal
* [upsert_portal_widget](docs/sdks/ecpadmin/README.md#upsert_portal_widget) - upsertPortalWidget

### [.balance](docs/sdks/balance/README.md)

* [get_customer_balance](docs/sdks/balance/README.md#get_customer_balance) - getCustomerBalance

### [.ecp](docs/sdks/ecp/README.md)

* [add_end_customer_relation_to_entity](docs/sdks/ecp/README.md#add_end_customer_relation_to_entity) - addEndCustomerRelationToEntity
* [create_custom_entity_activity](docs/sdks/ecp/README.md#create_custom_entity_activity) - createCustomEntityActivity
* [delete_entity_file](docs/sdks/ecp/README.md#delete_entity_file) - deleteEntityFile
* [delete_portal_user](docs/sdks/ecp/README.md#delete_portal_user) - deletePortalUser
* [get_all_contracts](docs/sdks/ecp/README.md#get_all_contracts) - getAllContracts
* [get_all_files](docs/sdks/ecp/README.md#get_all_files) - getAllFiles
* [get_all_opportunities](docs/sdks/ecp/README.md#get_all_opportunities) - getAllOpportunities
* [get_all_orders](docs/sdks/ecp/README.md#get_all_orders) - getAllOrders
* [get_billing_events](docs/sdks/ecp/README.md#get_billing_events) - getBillingEvents
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
* [track_file_downloaded](docs/sdks/ecp/README.md#track_file_downloaded) - trackFileDownloaded
* [trigger_entity_access](docs/sdks/ecp/README.md#trigger_entity_access) - triggerEntityAccess
* [update_contact](docs/sdks/ecp/README.md#update_contact) - updateContact
* [update_contract](docs/sdks/ecp/README.md#update_contract) - updateContract
* [update_opportunity](docs/sdks/ecp/README.md#update_opportunity) - updateOpportunity
* [update_order](docs/sdks/ecp/README.md#update_order) - updateOrder
* [update_portal_user](docs/sdks/ecp/README.md#update_portal_user) - updatePortalUser

### [.public](docs/sdks/public/README.md)

* [confirm_user](docs/sdks/public/README.md#confirm_user) - confirmUser
* [create_user](docs/sdks/public/README.md#create_user) - createUser
* [get_contact_count](docs/sdks/public/README.md#get_contact_count) - getContactCount
* [get_count_by_email](docs/sdks/public/README.md#get_count_by_email) - getCountByEmail
* [get_portal_config_by_domain](docs/sdks/public/README.md#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](docs/sdks/public/README.md#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_widgets](docs/sdks/public/README.md#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](docs/sdks/public/README.md#user_exists) - userExists

### [.activity](docs/sdks/activity/README.md)

* [get_entity_activity_feed](docs/sdks/activity/README.md#get_entity_activity_feed) - getEntityActivityFeed
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->



<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401,403,500      | application/json |
| errors.SDKError  | 400-600          | */*              |


## Example

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = None
try:
    res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)
except (errors.ErrorResp) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.object is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://customer-portal-api.sls.epilot.io` | None |

For example:

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    server_idx=0,
)


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    server_url="https://customer-portal-api.sls.epilot.io",
)


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->



<!-- Start Authentication -->

# Authentication

## Per-Client Security Schemes

Your SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |
| `portal_auth` | http          | HTTP Bearer   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```

## Per-Operation Security Schemes

Some operations in your SDK require the security scheme to be specified at the request level. For example:

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot()


res = s.ecp_admin.configure_distribution("", origin=components.Origin.INSTALLER_PORTAL)

if res.object is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
