# UploadFile201ApplicationJSON

Pre-signed URL for POST / PUT upload


## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      | Example                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `public_url`                                                                                                                     | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | Returned only if file is permanent i.e. file_entity_id is passed                                                                 | https://epilot-files-prod.s3.eu-central-1.amazonaws.com/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf                    |
| `s3ref`                                                                                                                          | [Optional[UploadFile201ApplicationJSONS3ref]](../../models/operations/uploadfile201applicationjsons3ref.md)                      | :heavy_minus_sign:                                                                                                               | N/A                                                                                                                              |                                                                                                                                  |
| `upload_url`                                                                                                                     | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | N/A                                                                                                                              | https://epilot-files-prod.s3.eu-central-1.amazonaws.com/123/temp/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf?AWSParams=123 |