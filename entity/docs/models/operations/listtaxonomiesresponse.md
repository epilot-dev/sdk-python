# ListTaxonomiesResponse


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                            | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `status_code`                                                                                             | *int*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `raw_response`                                                                                            | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                     | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `list_taxonomies_200_application_json_object`                                                             | [Optional[ListTaxonomies200ApplicationJSON]](../../models/operations/listtaxonomies200applicationjson.md) | :heavy_minus_sign:                                                                                        | Returns list of taxonomies in an organisation                                                             |