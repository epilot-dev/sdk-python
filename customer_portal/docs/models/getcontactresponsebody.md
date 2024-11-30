# GetContactResponseBody

Retrieves the mapped contact of the logged in user successfully.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `entity`                                                   | [Optional[models.Contact]](../models/contact.md)           | :heavy_minus_sign:                                         | The mapped contact of the portal user                      |
| `files`                                                    | List[[models.File](../models/file.md)]                     | :heavy_minus_sign:                                         | N/A                                                        |
| `journey_actions`                                          | List[[models.JourneyActions](../models/journeyactions.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `relations`                                                | List[[models.EntityItem](../models/entityitem.md)]         | :heavy_minus_sign:                                         | N/A                                                        |