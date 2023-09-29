# WorkflowExecutionCreateReq


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `assigned_to`                                                              | list[*str*]                                                                | :heavy_minus_sign:                                                         | N/A                                                                        |
| `contexts`                                                                 | list[[shared.WorkflowContext](undefined/models/shared/workflowcontext.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |
| `trigger`                                                                  | [Optional[shared.TriggerType]](undefined/models/shared/triggertype.md)     | :heavy_minus_sign:                                                         | N/A                                                                        |
| `workflow_id`                                                              | *Optional[str]*                                                            | :heavy_check_mark:                                                         | N/A                                                                        |