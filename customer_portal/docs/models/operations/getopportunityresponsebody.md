# GetOpportunityResponseBody

The returned opportunities


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `entity`                                                                   | [Optional[components.Opportunity]](../../models/components/opportunity.md) | :heavy_minus_sign:                                                         | The opportunity entity                                                     |
| `files`                                                                    | List[[components.File](../../models/components/file.md)]                   | :heavy_minus_sign:                                                         | The related files of the requested opportunity                             |
| `orders`                                                                   | List[[components.Order](../../models/components/order.md)]                 | :heavy_minus_sign:                                                         | The related orders of the requested opportunity                            |
| `relations`                                                                | List[[components.EntityItem](../../models/components/entityitem.md)]       | :heavy_minus_sign:                                                         | The related entities of the requested opportunity                          |
| `workflow`                                                                 | List[Dict[str, *Any*]]                                                     | :heavy_minus_sign:                                                         | The related workflows of the requested opportunity                         |