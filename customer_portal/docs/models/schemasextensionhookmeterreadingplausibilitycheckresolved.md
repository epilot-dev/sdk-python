# SchemasExtensionHookMeterReadingPlausibilityCheckResolved

Response to the call


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `lower_limit`                                   | *Optional[str]*                                 | :heavy_minus_sign:                              | Lower allowed limit of the meter reading        | {{CallResponse.data.lower_limit}}               |
| `upper_limit`                                   | *Optional[str]*                                 | :heavy_minus_sign:                              | Upper allowed limit of the meter reading        | {{CallResponse.data.upper_limit}}               |
| `valid`                                         | *Optional[str]*                                 | :heavy_minus_sign:                              | Indicate whether the meter reading is plausible | {{CallResponse.data.valid}}                     |