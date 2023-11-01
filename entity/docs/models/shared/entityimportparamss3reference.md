# EntityImportParamsS3Reference

The S3 bucket and key where the JSON file for import is located.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The name of the S3 bucket where the JSON file for import is stored. | my-bucket                                                           |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The key or path to the JSON file within the S3 bucket.              | imports/my-import.json                                              |