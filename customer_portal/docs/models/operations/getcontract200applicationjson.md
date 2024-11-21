# GetContract200ApplicationJSON

The requested contract returned successfully.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `entity`                                                     | [Optional[shared.Contract]](../../models/shared/contract.md) | :heavy_minus_sign:                                           | The contract entity                                          |
| `files`                                                      | List[[shared.File](../../models/shared/file.md)]             | :heavy_minus_sign:                                           | The related files of the requested contract                  |
| `orders`                                                     | List[[shared.Order](../../models/shared/order.md)]           | :heavy_minus_sign:                                           | The related orders of the requested contract                 |
| `relations`                                                  | List[[shared.EntityItem](../../models/shared/entityitem.md)] | :heavy_minus_sign:                                           | The related entities of the requested contract               |
| `workflow`                                                   | List[Dict[str, *Any*]]                                       | :heavy_minus_sign:                                           | N/A                                                          |