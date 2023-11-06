# TotalDetailsBreakdown

Breakdown of individual tax (and discount) amounts that add up to the totals.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `recurrences`                                                                            | List[[Union[RecurrenceAmount]](../../models/shared/totaldetailsbreakdownrecurrences.md)] | :heavy_minus_sign:                                                                       | The aggregated price items tax amount per rate.                                          |
| `taxes`                                                                                  | List[[Union[TaxAmountBreakdown]](../../models/shared/totaldetailsbreakdowntaxes.md)]     | :heavy_minus_sign:                                                                       | The aggregated price items tax amount per rate.                                          |