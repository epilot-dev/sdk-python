# WorkflowExecutionCreateReq

Workflow Execution payload


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `assigned_to`                                                   | list[*str*]                                                     | :heavy_minus_sign:                                              | N/A                                                             |
| `contexts`                                                      | list[[WorkflowContext](../../models/shared/workflowcontext.md)] | :heavy_minus_sign:                                              | N/A                                                             |
| `trigger`                                                       | [Optional[TriggerType]](../../models/shared/triggertype.md)     | :heavy_minus_sign:                                              | N/A                                                             |
| `workflow_id`                                                   | *str*                                                           | :heavy_check_mark:                                              | N/A                                                             |