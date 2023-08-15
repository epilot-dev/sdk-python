# ConfigureDistributionResponse


## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                          | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `error_resp`                                                                                                            | [Optional[shared.ErrorResp]](../../models/shared/errorresp.md)                                                          | :heavy_minus_sign:                                                                                                      | Could not authenticate the user                                                                                         |
| `status_code`                                                                                                           | *int*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `raw_response`                                                                                                          | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                   | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `configure_distribution_200_application_json_object`                                                                    | [Optional[ConfigureDistribution200ApplicationJSON]](../../models/operations/configuredistribution200applicationjson.md) | :heavy_minus_sign:                                                                                                      | The cloudfront distribution has been configure successfully for the custom domain.                                      |