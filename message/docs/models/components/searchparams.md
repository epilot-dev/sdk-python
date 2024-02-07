# SearchParams


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `q`                                                     | *str*                                                   | :heavy_check_mark:                                      | Lucene query syntax supported with ElasticSearch        | subject:"Request for solar panel price" AND _tags:INBOX |
| `from_`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `size`                                                  | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |                                                         |