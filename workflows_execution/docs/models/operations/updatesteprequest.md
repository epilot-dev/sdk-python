# UpdateStepRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `update_step_req`                                              | [shared.UpdateStepReq](../../models/shared/updatestepreq.md)   | :heavy_check_mark:                                             | Workflow Execution Step payload                                |
| `execution_id`                                                 | *str*                                                          | :heavy_check_mark:                                             | Id of the execution                                            |
| `step_id`                                                      | *str*                                                          | :heavy_check_mark:                                             | Short uuid (length 6) to identify the Workflow Execution Step. |