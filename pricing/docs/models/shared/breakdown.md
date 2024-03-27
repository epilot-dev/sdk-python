# Breakdown

Breakdown of individual tax (and discount) amounts that add up to the totals.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `recurrences`                                                                          | List[[Union[shared.RecurrenceAmount]](../../models/shared/totaldetailsrecurrences.md)] | :heavy_minus_sign:                                                                     | The aggregated price items tax amount per rate.                                        |
| `taxes`                                                                                | List[[Union[shared.TaxAmountBreakdown]](../../models/shared/totaldetailstaxes.md)]     | :heavy_minus_sign:                                                                     | The aggregated price items tax amount per rate.                                        |