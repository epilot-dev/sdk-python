# Deprecated
(*deprecated*)

### Available Operations

* [~~dollar_create_opportunity~~](#dollar_create_opportunity) - createOpportunity :warning: **Deprecated**

## ~~dollar_create_opportunity~~

This API is Deprecated. Please use the Entity API or Submission API to create opportunities.

Enables the creation of a new opportunity. During the creation of an opportunity, an unique customer-readable `opportunity_number` will be generated.
The `opportunity_number` can be used to universally identify an opportunity within epilot platform.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.deprecated.dollar_create_opportunity(opportunity=shared.OpportunityInput(
    additional_properties={
        "$ref": 'string',
    },
    tags=[
        'string',
    ],
    address=shared.OpportunityAddress(
        dollar_relation_ref=[
            shared.Opportunity1(),
        ],
    ),
    assignee=[
        shared.Assignee(
            email_notification_settings=shared.EmailNotificationSettings(),
        ),
    ],
    billing_address=shared.BillingAddress(
        dollar_relation_ref=[
            shared.OpportunitySchemas1(),
        ],
    ),
    customer=shared.OpportunityCustomer(
        dollar_relation=[
            shared.EntityRelation(
                additional_properties={
                    "key": 'string',
                },
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    dates=[
        shared.One(
            tags=[
                'string',
            ],
        ),
    ],
    delivery_address=shared.DeliveryAddress(
        dollar_relation_ref=[
            shared.OpportunitySchemasDeliveryAddress1(),
        ],
    ),
    items=shared.Items(
        dollar_relation=[
            shared.OrderRelation(
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    source=shared.OpportunitySource(
        http='/app/v2/journey-builder/editor/db7f6940-994b-11ec-a46d-9f1824ff2939',
        title='Journey: PH Journey',
    ),
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
), x_ivy_org_id='string')

if res.opportunity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `opportunity`                                                      | [shared.OpportunityInput](../../models/shared/opportunityinput.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `x_ivy_org_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The target Organization Id represented by the caller               |


### Response

**[operations.DollarCreateOpportunityResponse](../../models/operations/dollarcreateopportunityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 400-600          | */*              |
