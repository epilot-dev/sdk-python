# Files


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `s3ref`                                                          | [components.S3Reference](../../models/components/s3reference.md) | :heavy_check_mark:                                               | S3 Reference from File API                                       |
| `additional_properties`                                          | Dict[str, *Any*]                                                 | :heavy_minus_sign:                                               | N/A                                                              |
| `tags`                                                           | List[*str*]                                                      | :heavy_minus_sign:                                               | List of tags for File entities                                   |
| `filename`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Override the file name                                           |
| `relation_tags`                                                  | List[*str*]                                                      | :heavy_minus_sign:                                               | List of relation labels for File attachments                     |