# Error


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `cause`                                                      | *Optional[str]*                                              | :heavy_minus_sign:                                           | The cause of the error (visible for bad requests - http 400) |
| `message`                                                    | *str*                                                        | :heavy_check_mark:                                           | Error message                                                |
| `status`                                                     | *Optional[float]*                                            | :heavy_minus_sign:                                           | The HTTP status code                                         |