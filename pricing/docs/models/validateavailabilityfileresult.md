# ValidateAvailabilityFileResult

The availability map file result payload


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `errors`                                                                                 | List[[models.ValidateAvailabilityFileError](../models/validateavailabilityfileerror.md)] | :heavy_check_mark:                                                                       | The errors found on the file                                                             |
| `rules_parsed_count`                                                                     | *float*                                                                                  | :heavy_check_mark:                                                                       | The number of rules successfully parsed                                                  |
| `status`                                                                                 | [models.Status](../models/status.md)                                                     | :heavy_check_mark:                                                                       | The status of the validation                                                             |