# PutOrderResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `order`                                                            | [Optional[components.Order]](../../models/components/order.md)     | :heavy_minus_sign:                                                 | Order result                                                       | {<br/>"$ref": "#/components/examples/order-with-simple-prices"<br/>} |