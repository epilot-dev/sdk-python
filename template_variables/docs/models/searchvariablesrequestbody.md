# SearchVariablesRequestBody


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `query`                                          | *str*                                            | :heavy_check_mark:                               | Search string                                    | logo                                             |
| `template_type`                                  | [models.TemplateType](../models/templatetype.md) | :heavy_check_mark:                               | N/A                                              |                                                  |
| `entity_schemas`                                 | List[*str*]                                      | :heavy_minus_sign:                               | N/A                                              |                                                  |
| `from_`                                          | *Optional[int]*                                  | :heavy_minus_sign:                               | N/A                                              |                                                  |
| `lang`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | 2-letter language code (ISO 639-1)               |                                                  |
| `size`                                           | *Optional[int]*                                  | :heavy_minus_sign:                               | N/A                                              |                                                  |