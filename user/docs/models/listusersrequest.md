# ListUsersRequest


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `limit`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | Limit the results size                                |
| `offset`                                              | *Optional[float]*                                     | :heavy_minus_sign:                                    | Specify the offset                                    |
| `org_ids`                                             | List[*str*]                                           | :heavy_minus_sign:                                    | Comma-separated list of organization ids to filter by |
| `query`                                               | *Optional[str]*                                       | :heavy_minus_sign:                                    | Query text to filter by                               |