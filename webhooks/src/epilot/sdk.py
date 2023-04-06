"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .webhooks import Webhooks
from epilot.models import shared

SERVERS = [
    "https://webhooks.sls.epilot.io",
]
"""Contains the list of servers available to the SDK"""

class Epilot:
    r"""The epilot `Webhook service` provides the possibility to subscribe to epilot public events. This will allow you to receive notifications with payload to your configured webhook URL every time events happen in your account.
    This document describes the steps how to configure hooks, subscribe to events and how to manage those configurations. Service is reachable using https connection to ensure encryption between client and service.
    
    Webhooks can be comfortably configured and managed by admin users in epilot portal.
    
    # Available events
      For an overview about all events you can subscribe to with Webhooks you can call following endpoint `/webhooks/configured-events`. The response will contain a list of event names and their labels in form:
      * **eventName**: Name for identifying the event.
      * **eventLabel**: Either a user friendly label, or the eventName itself.
      When using the UI, you have the list of the available events in the drop down menu in webhook management form.
    Following Events are available for subscription:
      * [**customer request**](#tag/events_schema): generated on incoming requests from JB Journeys
    
    In [Events Schemas](#tag/events_schema) section you find the schemas of available events ready to register.
    
    # Create Webhook
      To secure your client server connection, please setup your webhook using endpoints supporting encryption, preferably [TLS](https://en.wikipedia.org/wiki/HTTPS). So we ensure encrypted data transfer to your server.
      An easy way to create webhook is to use the webhook ui in the epilot portal. You can set up your webhook configuration using the management form, and fill in there details about the webhook endpoint, event types and [authorization information](#section/Create-webhook/Authentication). However you still can use our API in the same way.
      To subscribe to an event using the API please use the `/v1/webhooks/configs` endpoint and post your receiver endpoint settings:
    
      | field | Required | Description |
      | ------- | --------| --------|
      | eventName  | required | epilot event you want to subscribe. see [Which events are available](#section/Create-Webhook/Which-events-are-available)|
      | url  | required | your endpoint where you want to receive the payload |
      | httpMethod | required | http method |
      | enabled | optional  |boolean whether the webhook is active or not |
      | auth | required |your endpoint authentication information. See [Authentication](#section/Create-Webhook/Authentication)|
      | filter  | optional |filter options, here you have the possibility to filter events, by product categories for example |
    
      ## Authentication
      We assume that your event handler endpoint is secured, we support currently following authentication types:
      * [Basic authentication](#section/Create-Webhook/Authentication/Basic-Authentication)
      * [Oauth](#section/Create-Webhook/Authentication/Oauth)
      * [API key](#section/Create-Webhook/Authentication/API-key)
    
      Further details on how to set up your authentication information using the API:
      ### Basic Authentication
    
      If you are using basic authentication you can set up the `auth` field
      | field | Required | Description |
      | ------- | --------| --------|
      | authType | required | \"BASIC\" |
      | basicAuthConfig | required | object only if authType is BASIC |
    
      **basicAuthConfig**:
      | field | Required | Description |
      | ------- | --------| --------|
      | username | required | valid username for your endpoint |
      | password | required | password |
    
      ### Oauth
    
      In case your endpoint is secured using Oauth your `Auth` should have following structure:
      | field | Required | Description |
      | ------- | --------| --------|
      | authType | required | \"OAUTH_CLIENT_CREDENTIALS\" |
      | oauthConfig | required | object only if authType is OAUTH_CLIENT_CREDENTIALS |
    
      **oauthConfig**:
      | field | Required | Description |
      | ------- | --------| --------|
      | clientId | required | your app Oauth client Id |
      | clientSecret | required | Oauth client secret |
      | endpoint | required | HTTPS endpoint for authentication |
      | httpMethod | required | HTTP methods like GET, POST... |
    
      ### API key
    
      We support also endpoints secured using API keys. In this case your webhook set up could be configured this way:
    
      | field | Required | Description |
      | ------- | --------| --------|
      | authType * | \"API_KEY\" |
      | apiKeyConfig * | object only if authType is API_KEY |
    
      **apiKeyConfig**:
      | field | Required | Description |
      | ------- | --------| --------|
      | keyName | required | used key name |
      | keyValue | required | value of the used key |
    
      ## Enable Filtering
    
      For better software integration you have the possibility to set up more granular filter for your subscribed events. For this please make use of the filter option when you create a webhook.
      Please note that the entire event will be sent when the filter matches.
    
      Using our ui in epilot portal, you can enable the filter option, and select items to be filtered.
    
      Using the webhook API, here more details about the possible and required fields.
    
      | field | Required | Description |
      | ------- | --------| --------|
      | keyToFilter | required | field of payload you want to filter |
      | supportedValues | required | list of values you want to receive |
    
      The subscribed events are simply a json structure, to have a filter in place for specific field in the event, you just set the `keyToFilter` value to be the field attribute structure of the json.
    
      For example you have the following event structure and you want your filter to apply only auth type :
    
      ```
      keyToFilter: {
        id,
        name,
        security{
          auth{
            type // basic|apikey|oauth|none
          }
        }
      }
      ```
    
      the `keyToFilter` should be `keyToFilter.security.auth`. And possible values should be set in `supportedValues` field.
    
      Please note that the `supportedValues` are **case sensitive**.
    
      Following example will filter this sample event to send only events having auth types basic and oauth.
    
      ```
       filter: {
          keyToFilter: 'keyToFilter.security.auth',
          supportedValues: ['basic','oauth']
        }
      ```
    
      **Sample filter:**
    
      For `Customer request` event you can filter events and receive only events related to specific product category:
      ```
       filter: {
          keyToFilter: 'customer_request.request_items.product_category',
          supportedValues: ['solar','electricity']
        }
      ```
    
      # List configured webhooks
    
      The `/v1/webhooks/configs` endpoint provides the list of the configured webhooks by your organization in following structure:
    
      | field | Description |
      | ------- | --------|
      |id	| webhook id |
      |eventName	|subscribed event name|
      |url |	configured client endpoint Url|
      |creationTime| webhook creation time|
      |httpMethod	| configured http method|
      |enabled	| boolean whether the webhook is enabled or not|
      |auth	| Auth settings if set|
      |filter	| filter settings if set|
    
      # Delete webhook
      To delete configured webhook using the ui, just hit the delete button for the wanted webhook configuration.
      To delete a webhook configuration using the API please use the `/v1/webhooks/configs/{WebhookId}` endpoint with `DELETE` http call.
    
      After deleting a webhook configuration you are still able to fetch failed and successfully sent events related to the deleted configuration.
    
      To retrieve webhook id you can query the configured webhooks, see [List configured Webhooks](#section/List-configured-Webhooks).
    
      # Edit Webhook
      Using the ui in the epilot portal you can very easily edit a webhook config. You will be asked to edit the pre filled form.
      To update a webhook configuration using the API please use following endpoint `/v1/webhooks/configs/{WebhookId}` using `PUT` http method.
      To retrieve webhook id you can query the configured webhooks, see [List configured Webhooks](#section/List-configured-Webhooks).
    
      Additional to this path parameters, the payload to update the webhook configuration is the same we use for creating new webhooks. You can also refer to [Which events are available](#section/Create-Webhook) for more details.
    
      To deactivate or reactivate a webhook configuration, you can make use of this endpoint, providing the organization id and webhook id as path parameter, and your payload should contain same configuration saved except the field `enabled` should either `false` if you want to deactivate the webhook otherwise `true` if the webhook should be active.
    """
    webhooks: Webhooks

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.3.0"
    _gen_version: str = "2.17.8"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    