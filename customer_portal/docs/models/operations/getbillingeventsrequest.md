# GetBillingEventsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `date_after`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `date_before`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `entity_id`                                                            | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `event_type`                                                           | [Optional[operations.EventType]](../../models/operations/eventtype.md) | :heavy_minus_sign:                                                     | Type of billing event to filter by                                     |