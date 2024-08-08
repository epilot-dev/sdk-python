# TotalDetails

The total details with tax (and discount) aggregated totals.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `amount_shipping`                                                             | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | This is the sum of all the price item shipping amounts.                       |
| `amount_tax`                                                                  | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | This is the sum of all the price item tax amounts.                            |
| `breakdown`                                                                   | [Optional[models.Breakdown]](../models/breakdown.md)                          | :heavy_minus_sign:                                                            | Breakdown of individual tax (and discount) amounts that add up to the totals. |