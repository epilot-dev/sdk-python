# RetriggerActionRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `action_id`                                                  | *str*                                                        | :heavy_check_mark:                                           | Id of Action to retry.                                       | 9ec3711b-db63-449c-b894-54d5bb622a8f                         |
| `execution_id`                                               | *str*                                                        | :heavy_check_mark:                                           | Execution Id                                                 | 9baf184f-bc81-4128-bca3-d974c90a12c4                         |
| `retry_req`                                                  | [Optional[shared.RetryReq]](../../models/shared/retryreq.md) | :heavy_minus_sign:                                           | Retry request details.                                       |                                                              |