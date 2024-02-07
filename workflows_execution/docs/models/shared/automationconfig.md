# AutomationConfig

Configuration for automation execution to run


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `flow_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Id of the configured automation to run                               |
| `execution_id`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Id of the automation execution which ran                             |
| `execution_status`                                                   | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Status of Automation Execution. Types can be found in Automation API |