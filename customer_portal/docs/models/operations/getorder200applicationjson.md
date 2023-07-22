# GetOrder200ApplicationJSON

The requested order has been retrieved successfully.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `cross_sellable_products`                                  | list[dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related cross sellable products of the requested order |
| `entity`                                                   | dict[str, *Any*]                                           | :heavy_minus_sign:                                         | The order entity                                           |
| `files`                                                    | list[dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related files of the requested order                   |
| `products`                                                 | list[dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related products of the requested order                |
| `relations`                                                | list[dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related entities of the requested order                |
| `workflow`                                                 | list[dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related workflows of the requested order               |