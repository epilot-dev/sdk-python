# AvailabilityCheckParams

Availability check request payload


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `filters`                                                                        | [components.AvailabilityFilters](../../models/components/availabilityfilters.md) | :heavy_check_mark:                                                               | Availability filters dimensions                                                  |
| `products`                                                                       | List[*str*]                                                                      | :heavy_check_mark:                                                               | Products to check availability                                                   |