# GetOrderResponseBody

The requested order has been retrieved successfully.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `cross_sellable_products`                                  | List[[models.Product](../models/product.md)]               | :heavy_minus_sign:                                         | The related cross sellable products of the requested order |
| `entity`                                                   | [Optional[models.Order]](../models/order.md)               | :heavy_minus_sign:                                         | The order entity                                           |
| `files`                                                    | List[[models.File](../models/file.md)]                     | :heavy_minus_sign:                                         | The related files of the requested order                   |
| `journey_actions`                                          | List[[models.JourneyActions](../models/journeyactions.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `products`                                                 | List[[models.Product](../models/product.md)]               | :heavy_minus_sign:                                         | The related products of the requested order                |
| `relations`                                                | List[[models.EntityItem](../models/entityitem.md)]         | :heavy_minus_sign:                                         | The related entities of the requested order                |
| `workflow`                                                 | List[Dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related workflows of the requested order               |