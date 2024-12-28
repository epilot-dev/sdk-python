# GetGroupsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `hydrate`                                                              | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Pass it true when you want to hydrate the group with full user details |
| `limit`                                                                | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Limit the results size                                                 |
| `offset`                                                               | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Specify the offset                                                     |
| `query`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Query name to filter by                                                |