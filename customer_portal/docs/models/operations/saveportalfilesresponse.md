# SavePortalFilesResponse


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `error_resp`                                                                                                | [Optional[shared.ErrorResp]](../../models/shared/errorresp.md)                                              | :heavy_minus_sign:                                                                                          | The request could not be validated                                                                          |
| `status_code`                                                                                               | *int*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `raw_response`                                                                                              | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                       | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `save_portal_files_201_application_json_object`                                                             | [Optional[SavePortalFiles201ApplicationJSON]](../../models/operations/saveportalfiles201applicationjson.md) | :heavy_minus_sign:                                                                                          | The files have been saved to the portal successfully.                                                       |