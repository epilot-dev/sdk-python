# ComputePriceResult


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `amount_total`                                                                         | *float*                                                                                | :heavy_check_mark:                                                                     | The computed total price                                                               |                                                                                        |
| `amount_total_decimal`                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | The computed total price as decimal                                                    |                                                                                        |
| `billing_period`                                                                       | [models.ComputePriceResultBillingPeriod](../models/computepriceresultbillingperiod.md) | :heavy_check_mark:                                                                     | The billing period                                                                     |                                                                                        |
| `breakdown`                                                                            | [models.ComputedPriceBreakdown](../models/computedpricebreakdown.md)                   | :heavy_check_mark:                                                                     | Price breakdown                                                                        |                                                                                        |
| `currency`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | The currency of the computed price (three-letter ISO currency code)                    | EUR                                                                                    |
| `meta`                                                                                 | [Optional[models.SignatureMeta]](../models/signaturemeta.md)                           | :heavy_minus_sign:                                                                     | Signature meta data payload                                                            |                                                                                        |
| `amount_static`                                                                        | *Optional[float]*                                                                      | :heavy_minus_sign:                                                                     | The computed static price                                                              |                                                                                        |
| `amount_static_decimal`                                                                | *Optional[Any]*                                                                        | :heavy_minus_sign:                                                                     | The computed static price as decimal                                                   |                                                                                        |
| `amount_variable_decimal_ht`                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The computed variable price, for the day period, as decimal                            |                                                                                        |
| `amount_variable_decimal_nt`                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The computed variable price, for the night period, as decimal                          |                                                                                        |
| `amount_variable_ht`                                                                   | *Optional[float]*                                                                      | :heavy_minus_sign:                                                                     | The computed variable price, for the day period                                        |                                                                                        |
| `amount_variable_nt`                                                                   | *Optional[float]*                                                                      | :heavy_minus_sign:                                                                     | The computed variable price, for the night period                                      |                                                                                        |