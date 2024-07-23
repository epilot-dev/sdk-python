# GetDefinitionsResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [components.HTTPMetadata](../../models/components/httpmetadata.md)                   | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `classes`                                                                            | List[[components.WorkflowDefinition](../../models/components/workflowdefinition.md)] | :heavy_minus_sign:                                                                   | Success - definitions loaded with success. Empty array if org has no definitions.    |