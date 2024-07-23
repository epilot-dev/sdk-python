# GetAllClosingReasonsResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [components.HTTPMetadata](../../models/components/httpmetadata.md)               | :heavy_check_mark:                                                               | N/A                                                                              |
| `closing_reasons`                                                                | [Optional[components.ClosingReasons]](../../models/components/closingreasons.md) | :heavy_minus_sign:                                                               | Returns the entire catalog of closing reasons per organization                   |