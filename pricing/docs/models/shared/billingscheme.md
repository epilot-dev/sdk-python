# BillingScheme

Describes how to compute the price per period. Either `per_unit` or `tiered`.
- `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
- `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the tiers and tiers_mode attributes.

⚠️ Tiered pricing is **not supported** yet.



## Values

| Name       | Value      |
| ---------- | ---------- |
| `PER_UNIT` | per_unit   |