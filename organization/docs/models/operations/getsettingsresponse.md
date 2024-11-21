# GetSettingsResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `settings`                                                         | Dict[str, *Any*]                                                   | :heavy_minus_sign:                                                 | Returns the organization settings                                  | {<br/>"double_opt_in": {<br/>"enabled": true<br/>}<br/>}           |