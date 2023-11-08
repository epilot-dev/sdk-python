# GetOrderResponseBody

The requested order has been retrieved successfully.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `cross_sellable_products`                                        | List[[components.Product](../../models/shared/product.md)]       | :heavy_minus_sign:                                               | The related cross sellable products of the requested order       |
| `entity`                                                         | [Optional[components.Order]](../../models/shared/order.md)       | :heavy_minus_sign:                                               | The order entity                                                 |
| `files`                                                          | List[[components.File](../../models/shared/file.md)]             | :heavy_minus_sign:                                               | The related files of the requested order                         |
| `products`                                                       | List[[components.Product](../../models/shared/product.md)]       | :heavy_minus_sign:                                               | The related products of the requested order                      |
| `relations`                                                      | List[[components.EntityItem](../../models/shared/entityitem.md)] | :heavy_minus_sign:                                               | The related entities of the requested order                      |
| `workflow`                                                       | List[Dict[str, *Any*]]                                           | :heavy_minus_sign:                                               | The related workflows of the requested order                     |