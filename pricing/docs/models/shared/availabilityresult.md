# AvailabilityResult

The availability check result payload


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `available_products`                                                                          | list[*str*]                                                                                   | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `check_results`                                                                               | list[[AvailabilityResultCheckResults](../../models/shared/availabilityresultcheckresults.md)] | :heavy_minus_sign:                                                                            | The check result details                                                                      |