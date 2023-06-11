# MessageRequestParamsThread

Open new thread when sending the very first message in conversation. Thread should contains context related to all messages in it (eg. topic, brand_id, opportunity_id, assigned_to,...).\
Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing.\
`thread` or `parent_id` must be provided either.



## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `assigned_to`                                                                         | list[*str*]                                                                           | :heavy_minus_sign:                                                                    | Ivy User ID of who the message is assigned to. Default is the user who sends message. |
| `topic`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | Message topic (e.g. which service sends the message or message category)              |