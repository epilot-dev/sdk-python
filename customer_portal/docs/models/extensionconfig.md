# ExtensionConfig


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Name of the extension                                                        |
| `options`                                                                    | Dict[str, *str*]                                                             | :heavy_minus_sign:                                                           | Extension option values.                                                     |
| `status`                                                                     | [Optional[models.ExtensionConfigStatus]](../models/extensionconfigstatus.md) | :heavy_minus_sign:                                                           | Status of the extension                                                      |