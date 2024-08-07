# epilot-customer-portal

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=customer_portal
```

Poetry
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_customer_portal
from epilot_customer_portal import Epilot

async def main():
    s = Epilot(
        security=epilot_customer_portal.Security(
            either_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.ecp_admin.can_trigger_portal_flow_async(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, trigger_portal_flow={
        "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

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
* [get_portal_widgets](docs/sdks/ecpadmin/README.md#get_portal_widgets) - getPortalWidgets
* [get_recipients_to_notify_on_automation](docs/sdks/ecpadmin/README.md#get_recipients_to_notify_on_automation) - getRecipientsToNotifyOnAutomation
* [get_registration_identifiers](docs/sdks/ecpadmin/README.md#get_registration_identifiers) - getRegistrationIdentifiers
* [get_valid_secondary_attributes](docs/sdks/ecpadmin/README.md#get_valid_secondary_attributes) - getValidSecondaryAttributes
* [login_to_portal_as_user](docs/sdks/ecpadmin/README.md#login_to_portal_as_user) - loginToPortalAsUser
* [replace_ecp_template_variables](docs/sdks/ecpadmin/README.md#replace_ecp_template_variables) - replaceECPTemplateVariables
* [save_portal_files](docs/sdks/ecpadmin/README.md#save_portal_files) - savePortalFiles
* [upsert_email_templates](docs/sdks/ecpadmin/README.md#upsert_email_templates) - upsertEmailTemplates
* [upsert_portal](docs/sdks/ecpadmin/README.md#upsert_portal) - upsertPortal
* [upsert_portal_widget](docs/sdks/ecpadmin/README.md#upsert_portal_widget) - upsertPortalWidget

### [balance](docs/sdks/balancesdk/README.md)

* [get_customer_balance](docs/sdks/balancesdk/README.md#get_customer_balance) - getCustomerBalance

### [ecp](docs/sdks/ecp/README.md)

* [add_contract_by_identifiers](docs/sdks/ecp/README.md#add_contract_by_identifiers) - addContractByIdentifiers
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
* [get_external_links](docs/sdks/ecp/README.md#get_external_links) - getExternalLinks
* [get_file_by_id](docs/sdks/ecp/README.md#get_file_by_id) - getFileById
* [get_files_count_by_entity](docs/sdks/ecp/README.md#get_files_count_by_entity) - getFileCountByEntity
* [get_opportunity](docs/sdks/ecp/README.md#get_opportunity) - getOpportunity
* [get_order](docs/sdks/ecp/README.md#get_order) - getOrder
* [get_organization_settings](docs/sdks/ecp/README.md#get_organization_settings) - getOrganizationSettings
* [get_portal_config](docs/sdks/ecp/README.md#get_portal_config) - getPortalConfig
* [get_portal_user](docs/sdks/ecp/README.md#get_portal_user) - getPortalUser
* [get_portal_widgets](docs/sdks/ecp/README.md#get_portal_widgets) - getPortalWidgets
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

### [activity](docs/sdks/activity/README.md)

* [get_entity_activity_feed](docs/sdks/activity/README.md#get_entity_activity_feed) - getEntityActivityFeed

### [public](docs/sdks/public/README.md)

* [check_contact_exists](docs/sdks/public/README.md#check_contact_exists) - checkContactExists
* [confirm_user](docs/sdks/public/README.md#confirm_user) - confirmUser
* [confirm_user_with_user_id](docs/sdks/public/README.md#confirm_user_with_user_id) - confirmUserWithUserId
* [create_user](docs/sdks/public/README.md#create_user) - createUser
* [get_portal_config_by_domain](docs/sdks/public/README.md#get_portal_config_by_domain) - getPortalConfigByDomain
* [get_public_portal_config](docs/sdks/public/README.md#get_public_portal_config) - getPublicPortalConfig
* [get_public_portal_widgets](docs/sdks/public/README.md#get_public_portal_widgets) - getPublicPortalWidgets
* [user_exists](docs/sdks/public/README.md#user_exists) - userExists
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.ecp_admin.can_trigger_portal_flow(origin=epilot_customer_portal.Origin.END_CUSTOMER_PORTAL, trigger_portal_flow={
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401,403,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot, models

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = None
try:
    res = s.ecp_admin.configure_distribution(origin=epilot_customer_portal.Origin.INSTALLER_PORTAL)

except models.ErrorResp as e:
    # handle exception
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://customer-portal-api.sls.epilot.io` | None |

#### Example

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    server_url="https://customer-portal-api.sls.epilot.io",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_customer_portal import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_customer_portal import Epilot
from epilot_customer_portal.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Epilot(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `either_auth` | http          | HTTP Bearer   |
| `epilot_auth` | http          | HTTP Bearer   |
| `portal_auth` | http          | HTTP Bearer   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
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
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_customer_portal import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_customer_portal"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
