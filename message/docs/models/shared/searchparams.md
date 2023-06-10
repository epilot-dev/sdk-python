# SearchParams


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `from_`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `q`                                                     | *str*                                                   | :heavy_check_mark:                                      | Lucene query syntax supported with ElasticSearch        | subject:"Request for solar panel price" AND _tags:INBOX |
| `size`                                                  | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |