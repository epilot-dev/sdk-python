# GetContractResponseBody

The requested contract returned successfully.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `entity`                                                   | [Optional[models.Contract]](../models/contract.md)         | :heavy_minus_sign:                                         | The contract entity                                        |
| `files`                                                    | List[[models.File](../models/file.md)]                     | :heavy_minus_sign:                                         | The related files of the requested contract                |
| `journey_actions`                                          | List[[models.JourneyActions](../models/journeyactions.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `meters`                                                   | List[[models.Meter](../models/meter.md)]                   | :heavy_minus_sign:                                         | The related meters of the requested contract               |
| `orders`                                                   | List[[models.Order](../models/order.md)]                   | :heavy_minus_sign:                                         | The related orders of the requested contract               |
| `relations`                                                | List[[models.EntityItem](../models/entityitem.md)]         | :heavy_minus_sign:                                         | The related entities of the requested contract             |
| `workflow`                                                 | List[Dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | N/A                                                        |