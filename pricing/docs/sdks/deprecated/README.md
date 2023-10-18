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
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DollarCreateOpportunityRequest(
    opportunity_input=shared.OpportunityInput(
        additional_properties={
            "$ref": 'Sulfur',
        },
        tags=[
            'Lari',
        ],
        address=shared.OpportunityAddress(
            dollar_relation_ref=[
                shared.OpportunityAddressDollarRelationRef1(),
            ],
        ),
        assignee=[
            shared.OpportunityAssignee(
                email_notification_settings=shared.OpportunityAssigneeEmailNotificationSettings(),
            ),
        ],
        billing_address=shared.OpportunityBillingAddress(
            dollar_relation_ref=[
                shared.OpportunityBillingAddressDollarRelationRef1(),
            ],
        ),
        customer=shared.OpportunityCustomer(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        "Berkelium": 'under',
                    },
                    tags=[
                        'color',
                    ],
                ),
            ],
        ),
        dates=[
            shared.OpportunityDates1(
                tags=[
                    'Hybrid',
                ],
            ),
        ],
        delivery_address=shared.OpportunityDeliveryAddress(
            dollar_relation_ref=[
                shared.OpportunityDeliveryAddressDollarRelationRef1(),
            ],
        ),
        items=shared.OpportunityItems(
            dollar_relation=[
                shared.OrderRelation(
                    tags=[
                        'South',
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
    ),
    x_ivy_org_id='West',
)

res = s.deprecated.dollar_create_opportunity(req)

if res.opportunity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DollarCreateOpportunityRequest](../../models/operations/dollarcreateopportunityrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DollarCreateOpportunityResponse](../../models/operations/dollarcreateopportunityresponse.md)**

