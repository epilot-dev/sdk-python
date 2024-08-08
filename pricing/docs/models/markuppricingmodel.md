# MarkupPricingModel

Describes how to compute the markup per period. Either `per_unit`, `tiered_volume` or `tiered_flatfee`.
- `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
- `tiered_volume` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unitary price for all purchased units.
- `tiered_flatfee` While similar to tiered_volume, tiered flat fee charges for the same price (flat) for the entire range instead using the unit price to multiply the quantity.



## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `PER_UNIT`       | per_unit         |
| `TIERED_VOLUME`  | tiered_volume    |
| `TIERED_FLATFEE` | tiered_flatfee   |