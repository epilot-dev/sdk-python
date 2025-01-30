# ValidateCaaRecordsResponseBody

Validated CAA records successfully.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `is_dns_configured`                                          | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Whether the DNS is configured from the customer side         |
| `message`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | Message of the validation                                    |
| `retry`                                                      | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Whether to retry the validation to continue the domain setup |