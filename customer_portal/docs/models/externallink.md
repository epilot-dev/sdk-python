# ExternalLink


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | Unique identifier for the external link                     |
| `label`                                                     | Dict[str, *str*]                                            | :heavy_check_mark:                                          | N/A                                                         |
| `link`                                                      | *str*                                                       | :heavy_check_mark:                                          | The URL of the external link                                |
| `type`                                                      | [models.ExternalLinkType](../models/externallinktype.md)    | :heavy_check_mark:                                          | N/A                                                         |
| `attribute`                                                 | *Optional[str]*                                             | :heavy_minus_sign:                                          | Attribute associated with the link                          |
| `attribute_value`                                           | *Optional[str]*                                             | :heavy_minus_sign:                                          | Attribute value for the link                                |
| `entity`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | Entity associated with the link                             |
| `extension_link_id`                                         | List[*str*]                                                 | :heavy_minus_sign:                                          | Seamless link identifier in a form of [extensionId, linkId] |
| `icon`                                                      | [Optional[models.Icon]](../models/icon.md)                  | :heavy_minus_sign:                                          | Configuration of the icon for the external link             |
| `rules`                                                     | List[[models.Rules](../models/rules.md)]                    | :heavy_minus_sign:                                          | N/A                                                         |