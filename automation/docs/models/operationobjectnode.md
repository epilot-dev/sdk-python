# OperationObjectNode


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `__pydantic_extra__`                           | Dict[str, *Any*]                               | :heavy_minus_sign:                             | N/A                                            |                                                |
| `append`                                       | List[*Any*]                                    | :heavy_minus_sign:                             | Append to array                                |                                                |
| `copy`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Copy JSONPath value from source entity context | contact.first_name                             |
| `set`                                          | *Optional[Any]*                                | :heavy_minus_sign:                             | N/A                                            |                                                |
| `uniq`                                         | [Optional[models.Uniq]](../models/uniq.md)     | :heavy_minus_sign:                             | Unique array                                   |                                                |