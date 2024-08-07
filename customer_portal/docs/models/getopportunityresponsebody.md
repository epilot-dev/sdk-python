# GetOpportunityResponseBody

The returned opportunities


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `entity`                                                   | [Optional[models.Opportunity]](../models/opportunity.md)   | :heavy_minus_sign:                                         | The opportunity entity                                     |
| `files`                                                    | List[[models.File](../models/file.md)]                     | :heavy_minus_sign:                                         | The related files of the requested opportunity             |
| `journey_actions`                                          | List[[models.JourneyActions](../models/journeyactions.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `orders`                                                   | List[[models.Order](../models/order.md)]                   | :heavy_minus_sign:                                         | The related orders of the requested opportunity            |
| `relations`                                                | List[[models.EntityItem](../models/entityitem.md)]         | :heavy_minus_sign:                                         | The related entities of the requested opportunity          |
| `workflow`                                                 | List[Dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | The related workflows of the requested opportunity         |