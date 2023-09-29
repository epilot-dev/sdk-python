# AvailabilityCheckParams

Availability check request payload


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `filters`                                                                              | [Optional[shared.AvailabilityFilters]](undefined/models/shared/availabilityfilters.md) | :heavy_check_mark:                                                                     | Availability filters dimensions                                                        |
| `products`                                                                             | list[*str*]                                                                            | :heavy_check_mark:                                                                     | Products to check availability                                                         |