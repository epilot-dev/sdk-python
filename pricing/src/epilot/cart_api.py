"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import errors, operations, shared
from typing import Optional

class CartAPI:
    r"""Used to interact with a cart during a customer's checkout session, providing:
     - An unified data model to model a Shopping Cart
     - Product and pricing data validation
     - Checkout a cart into an order or quote
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def dollar_checkout_cart(self, request: operations.DollarCheckoutCartRequest) -> operations.DollarCheckoutCartResponse:
        r"""checkoutCart
        Checkouts a cart and executes the specified checkout `mode` process.

        A Checkout implicitly finalizes the provided cart (if not transient from a fast-checkout) and behaves in one of the following modes:
        - `create_order` (**default**): the payment happens at a later date or managed by 3rd-party CRM (SAP)
        - `create_invoice`: the payment happens on the online checkout (paypal, stripe, adyen)
        - `create_quote`: the checkout represents a price quote request

        Fast checkout is also supported, by passing the Cart contents directly.
        When a fast checkout is performed the cart is considered transient and there is no cart persistance.

        If the checkout `mode` is omitted, the `mode` will default to `create_order`.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/public/cart:checkout'
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "checkout_cart", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DollarCheckoutCartResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CheckoutCartResult])
                res.checkout_cart_result = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    