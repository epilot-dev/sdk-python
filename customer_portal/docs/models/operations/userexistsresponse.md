# UserExistsResponse


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `error_resp`                                                                                      | [Optional[shared.ErrorResp]](../../models/shared/errorresp.md)                                    | :heavy_minus_sign:                                                                                | Internal Server Error                                                                             |
| `status_code`                                                                                     | *int*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `raw_response`                                                                                    | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)             | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `user_exists_200_application_json_object`                                                         | [Optional[UserExists200ApplicationJSON]](../../models/operations/userexists200applicationjson.md) | :heavy_minus_sign:                                                                                | Returned whether the user exists in the portal or not successfully.                               |