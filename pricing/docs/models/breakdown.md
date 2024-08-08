# Breakdown

Breakdown of individual tax (and discount) amounts that add up to the totals.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `recurrences`                                                                | List[[models.TotalDetailsRecurrences](../models/totaldetailsrecurrences.md)] | :heavy_minus_sign:                                                           | The aggregated price items tax amount per rate.                              |
| `recurrences_by_tax`                                                         | List[[models.RecurrencesByTax](../models/recurrencesbytax.md)]               | :heavy_minus_sign:                                                           | The aggregated price items recurrences by tax rate                           |
| `taxes`                                                                      | List[[models.TotalDetailsTaxes](../models/totaldetailstaxes.md)]             | :heavy_minus_sign:                                                           | The aggregated price items tax amount per rate.                              |