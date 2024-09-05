# GetNotificationsV2ResponseBody

Success


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `cursor`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | Base64 encoded cursor to be used for pagination                | eyJjcmVhd                                                      |
| `results`                                                      | List[[models.NotificationItem](../models/notificationitem.md)] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `total`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            | 1                                                              |
| `total_unread`                                                 | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            | 1                                                              |