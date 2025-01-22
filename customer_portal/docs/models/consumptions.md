# Consumptions


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `timestamp`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)             | :heavy_check_mark:                                                               | ISO 8601 timestamp of the consumption record.                                    |
| `value`                                                                          | *float*                                                                          | :heavy_check_mark:                                                               | The consumption value.                                                           |
| `type`                                                                           | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional type of the consumption, such as 'nt' (night time) or 'ht' (high time). |