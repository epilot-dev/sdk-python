# GetOpportunity200ApplicationJSON

The returned opportunities


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `entity`                                                           | [Optional[shared.Opportunity]](../../models/shared/opportunity.md) | :heavy_minus_sign:                                                 | The opportunity entity                                             |
| `files`                                                            | List[[shared.File](../../models/shared/file.md)]                   | :heavy_minus_sign:                                                 | The related files of the requested opportunity                     |
| `orders`                                                           | List[[shared.Order](../../models/shared/order.md)]                 | :heavy_minus_sign:                                                 | The related orders of the requested opportunity                    |
| `relations`                                                        | List[[shared.EntityItem](../../models/shared/entityitem.md)]       | :heavy_minus_sign:                                                 | The related entities of the requested opportunity                  |
| `workflow`                                                         | List[Dict[str, *Any*]]                                             | :heavy_minus_sign:                                                 | The related workflows of the requested opportunity                 |