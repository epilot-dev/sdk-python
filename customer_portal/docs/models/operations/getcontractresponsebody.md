# GetContractResponseBody

The requested contract returned successfully.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `entity`                                                         | [Optional[components.Contract]](../../models/shared/contract.md) | :heavy_minus_sign:                                               | The contract entity                                              |
| `files`                                                          | List[[components.File](../../models/shared/file.md)]             | :heavy_minus_sign:                                               | The related files of the requested contract                      |
| `orders`                                                         | List[[components.Order](../../models/shared/order.md)]           | :heavy_minus_sign:                                               | The related orders of the requested contract                     |
| `relations`                                                      | List[[components.EntityItem](../../models/shared/entityitem.md)] | :heavy_minus_sign:                                               | The related entities of the requested contract                   |
| `workflow`                                                       | List[Dict[str, *Any*]]                                           | :heavy_minus_sign:                                               | N/A                                                              |