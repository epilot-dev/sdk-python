# TriggerWorkflowConfig


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `assign_steps`                                                                 | List[[models.AssignUsersToStep](../models/assignuserstostep.md)]               | :heavy_minus_sign:                                                             | N/A                                                                            |
| `assignees`                                                                    | List[*str*]                                                                    | :heavy_minus_sign:                                                             | N/A                                                                            |
| `conditions`                                                                   | List[[models.TriggerWorkflowCondition](../models/triggerworkflowcondition.md)] | :heavy_minus_sign:                                                             | N/A                                                                            |
| `target_workflow`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |