# GenerateDocumentV2TemplateDocument

Input template document


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `filename`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Document original filename                                             | my-template-{{order.order_number}}.docx                                |
| `s3ref`                                                                | [Optional[components.S3Reference]](../../models/shared/s3reference.md) | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |