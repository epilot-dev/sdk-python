# RetryReq


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `condition_id`                                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The condition id to retry when retry strategy is RETRY_ALL_PARENT_CONDITION_ACTIONS |
| `retry_strategy`                                                                    | [Optional[models.RetryStrategy]](../models/retrystrategy.md)                        | :heavy_minus_sign:                                                                  | different behaviors for retrying failed execution actions.                          |