# VariableContext


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `brand`                                                     | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         | {"$ref":"#/components/examples/ExampleBrand/value"}         |
| `contact`                                                   | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         | {"$ref":"#/components/examples/ExampleContactEntity/value"} |
| `main`                                                      | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         | {"$ref":"#/components/examples/ExampleMain/value"}          |
| `unsubscribe_url`                                           | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         | https://consent.sls.epilot.io/v1/unsubscribe?token=abc123   |