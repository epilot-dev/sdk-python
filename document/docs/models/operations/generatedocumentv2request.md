# GenerateDocumentV2Request


## Fields

| Field                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                                                                                   | [Optional[operations.GenerateDocumentV2RequestBody]](../../models/operations/generatedocumentv2requestbody.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                              |
| `job_id`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                               | Job ID for tracking the status of document generation action                                                                                                                                                                                                     |
| `mode`                                                                                                                                                                                                                                                           | [Optional[operations.Mode]](../../models/operations/mode.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                               | Type of mode used for document generation flow.<br/>Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.<br/>Full - Goes through all the steps for the full generation of final document<br/> |