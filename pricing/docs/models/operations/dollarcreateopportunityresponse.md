# DollarCreateOpportunityResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `http_meta`                                                                | [components.HTTPMetadata](../../models/components/httpmetadata.md)         | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `opportunity`                                                              | [Optional[components.Opportunity]](../../models/components/opportunity.md) | :heavy_minus_sign:                                                         | The new Opportunity.                                                       | {<br/>"$ref": "#/components/examples/opportunity"<br/>}                    |