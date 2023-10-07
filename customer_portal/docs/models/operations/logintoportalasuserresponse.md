# LoginToPortalAsUserResponse


## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                                     | *Optional[str]*                                                                                                                    | :heavy_check_mark:                                                                                                                 | HTTP response content type for this operation                                                                                      |
| `status_code`                                                                                                                      | *Optional[int]*                                                                                                                    | :heavy_check_mark:                                                                                                                 | HTTP response status code for this operation                                                                                       |
| `raw_response`                                                                                                                     | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                              | :heavy_minus_sign:                                                                                                                 | Raw HTTP response; suitable for custom response parsing                                                                            |
| `login_to_portal_as_user_200_application_json_object`                                                                              | [Optional[operations.LoginToPortalAsUser200ApplicationJSON]](undefined/models/operations/logintoportalasuser200applicationjson.md) | :heavy_minus_sign:                                                                                                                 | The token has been generated successfully.                                                                                         |