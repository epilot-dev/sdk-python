# EntityOperation


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `entity`                                                 | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `operation`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | updateEntity                                             |
| `params`                                                 | [Optional[shared.Params]](../../models/shared/params.md) | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `payload`                                                | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      | {"_schema":"contact","_org":"123","status":"Inactive"}   |