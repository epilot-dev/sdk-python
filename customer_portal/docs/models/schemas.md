# Schemas

Hook that will allow using the specified source as data for consumption visualizations. This hook is triggered to fetch the data. Format of the request and response has to follow the following specification: TBD. The expected response to the call is:
  - 200 with the time series data



## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `call`                                                     | [models.Call](../models/call.md)                           | :heavy_check_mark:                                         | N/A                                                        |
| `type`                                                     | [models.Type](../models/type.md)                           | :heavy_check_mark:                                         | N/A                                                        |
| `auth`                                                     | [Optional[models.Auth]](../models/auth.md)                 | :heavy_minus_sign:                                         | N/A                                                        |
| `id`                                                       | *Optional[str]*                                            | :heavy_minus_sign:                                         | Identifier of the hook. Should not change between updates. |
| `resolved`                                                 | [Optional[models.Resolved]](../models/resolved.md)         | :heavy_minus_sign:                                         | N/A                                                        |