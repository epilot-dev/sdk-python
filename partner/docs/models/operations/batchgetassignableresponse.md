# BatchGetAssignableResponse


## Fields

| Field                                                                                                             | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                    | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `status_code`                                                                                                     | *int*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `raw_response`                                                                                                    | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                             | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `batch_get_assignable_200_application_json_object`                                                                | [Optional[BatchGetAssignable200ApplicationJSON]](../../models/operations/batchgetassignable200applicationjson.md) | :heavy_minus_sign:                                                                                                | List of assignable results                                                                                        |