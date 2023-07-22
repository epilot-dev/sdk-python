# PaymentMethod

A PaymentMethod represent your customer's payment instruments.



## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `details`                                                       | dict[str, *Any*]                                                | :heavy_minus_sign:                                              | Contains relevant data associated with the payment method type. |
| `type`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The type of the PaymentMethod.                                  |