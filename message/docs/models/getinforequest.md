# GetInfoRequest


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `thread_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Thread ID                                                             |
| `message_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Message ID, If not passed defaults to latest message ID in the thread |