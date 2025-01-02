# ExecItem

Execution item for bulk trigger automation. It maps each entity to its automation execution id & status


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `entity_id`                                            | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    | e3d3ebac-baab-4395-abf4-50b5bf1f8b74                   |
| `execution_status`                                     | [models.ExecutionStatus](../models/executionstatus.md) | :heavy_check_mark:                                     | N/A                                                    |                                                        |
| `entity_schema`                                        | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |                                                        |
| `error`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | Error message for the failed automation execution      |                                                        |
| `execution_id`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    | 9baf184f-bc81-4128-bca3-d974c90a12c4                   |