# PricePricingModel

Describes how to compute the price per period. Either `per_unit`, `tiered_graduated` or `tiered_volume`.
- `per_unit` indicates that the fixed amount (specified in unit_amount or unit_amount_decimal) will be charged per unit in quantity
- `tiered_graduated` indicates that the unit pricing will be computed using tiers attribute. The customer pays the price per unit in every range their purchase rises through.
- `tiered_volume` indicates that the unit pricing will be computed using tiers attribute. The customer pays the same unit price for all purchased units.
- `tiered_flatfee` While similar to tiered_volume, tiered flat fee charges for the same price (flat) for the entire range instead using the unit price to multiply the quantity.
- `external_getag` indicates that the price is influenced by aquisition fees provided by GetAG.



## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `PER_UNIT`         | per_unit           |
| `TIERED_GRADUATED` | tiered_graduated   |
| `TIERED_VOLUME`    | tiered_volume      |
| `TIERED_FLATFEE`   | tiered_flatfee     |
| `EXTERNAL_GETAG`   | external_getag     |