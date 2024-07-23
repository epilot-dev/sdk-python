# GetMaxAllowedLimitResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md)                 | :heavy_check_mark:                                                                 | N/A                                                                                |
| `max_allowed_limit`                                                                | [Optional[components.MaxAllowedLimit]](../../models/components/maxallowedlimit.md) | :heavy_minus_sign:                                                                 | A combo of current number of workflows, and the max allowed number of workflows.   |