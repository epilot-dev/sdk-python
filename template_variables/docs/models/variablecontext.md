# VariableContext


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `brand`                                                        | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            | {<br/>"$ref": "#/components/examples/ExampleBrand/value"<br/>} |
| `contact`                                                      | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            | {<br/>"$ref": "#/components/examples/ExampleContactEntity/value"<br/>} |
| `main`                                                         | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            | {<br/>"$ref": "#/components/examples/ExampleMain/value"<br/>}  |
| `unsubscribe_url`                                              | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | https://consent.sls.epilot.io/v1/unsubscribe?token=abc123      |