# Balance


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `balance`                                                         | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Current balance of the customer in cents. (precision 2)           | 8990                                                              |
| `balance_currency`                                                | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Currency code in ISO 4217 format                                  | EUR                                                               |
| `balance_decimal`                                                 | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Current balance of the customer in decimal string representation. | 89.90                                                             |