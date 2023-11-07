# Grant


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `action`                                                     | *str*                                                        | :heavy_check_mark:                                           | Action for granting permission                               | entity-read                                                  |
| `effect`                                                     | [Optional[components.Effect]](../../models/shared/effect.md) | :heavy_minus_sign:                                           | Effect of the permission                                     |                                                              |
| `resource`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | Resource for granting permission                             | entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947      |