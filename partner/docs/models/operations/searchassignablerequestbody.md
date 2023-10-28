# SearchAssignableRequestBody


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `from_`                                                                                               | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | start results from an offset for pagination                                                           |
| `org_ids`                                                                                             | List[*str*]                                                                                           | :heavy_minus_sign:                                                                                    | filter results to specific organizations. defaults to all orgs                                        |
| `q`                                                                                                   | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | search query to filter results                                                                        |
| `size`                                                                                                | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | limit number of results to return                                                                     |
| `types`                                                                                               | List[[SearchAssignableRequestBodyTypes](../../models/operations/searchassignablerequestbodytypes.md)] | :heavy_minus_sign:                                                                                    | filter results to specific types of assignables. defaults to all types                                |