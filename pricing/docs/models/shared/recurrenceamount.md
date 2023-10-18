# RecurrenceAmount

An amount associated with a specific recurrence.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `amount_subtotal`                                                                  | *int*                                                                              | :heavy_check_mark:                                                                 | Total of all items, with same recurrence, before (discounts or) taxes are applied. |
| `amount_tax`                                                                       | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Total of all items taxes, with same recurrence.                                    |
| `amount_total`                                                                     | *int*                                                                              | :heavy_check_mark:                                                                 | Total of all items, with same recurrence, after (discounts and) taxes are applied. |
| `billing_period`                                                                   | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The price billing period.                                                          |
| `type`                                                                             | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The price type.                                                                    |