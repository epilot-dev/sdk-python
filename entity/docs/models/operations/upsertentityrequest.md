# UpsertEntityRequest


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request_body`                                                                               | [Optional[UpsertEntityRequestBody]](../../models/operations/upsertentityrequestbody.md)      | :heavy_minus_sign:                                                                           | N/A                                                                                          |                                                                                              |
| `activity_id`                                                                                | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Activity to include in event feed                                                            | 01F130Q52Q6MWSNS8N2AVXV4JN                                                                   |
| `async_`                                                                                     | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Don't wait for updated entity to become available in Search API. Useful for large migrations |                                                                                              |
| `dry_run`                                                                                    | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Dry Run mode = return matched entities but don't update them.                                |                                                                                              |
| `slug`                                                                                       | *str*                                                                                        | :heavy_check_mark:                                                                           | Entity Schema                                                                                | contact                                                                                      |