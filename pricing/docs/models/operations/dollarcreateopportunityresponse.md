# DollarCreateOpportunityResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `error`                                                                               | [Optional[shared.Error]](../../models/shared/error.md)                                | :heavy_minus_sign:                                                                    | Invalid payload                                                                       |
| `opportunity`                                                                         | dict[str, *Any*]                                                                      | :heavy_minus_sign:                                                                    | The new Opportunity.                                                                  |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |