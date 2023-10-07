# GetAllContractsResponse


## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                             | *Optional[str]*                                                                                                            | :heavy_check_mark:                                                                                                         | HTTP response content type for this operation                                                                              |
| `error_resp`                                                                                                               | [Optional[shared.ErrorResp]](undefined/models/shared/errorresp.md)                                                         | :heavy_minus_sign:                                                                                                         | Could not authenticate the user                                                                                            |
| `status_code`                                                                                                              | *Optional[int]*                                                                                                            | :heavy_check_mark:                                                                                                         | HTTP response status code for this operation                                                                               |
| `raw_response`                                                                                                             | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                      | :heavy_minus_sign:                                                                                                         | Raw HTTP response; suitable for custom response parsing                                                                    |
| `get_all_contracts_200_application_json_object`                                                                            | [Optional[operations.GetAllContracts200ApplicationJSON]](undefined/models/operations/getallcontracts200applicationjson.md) | :heavy_minus_sign:                                                                                                         | Contracts have been retrieved successfully.                                                                                |