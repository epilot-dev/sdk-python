# DisableDetails


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `disabled_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the flow was disabled                                           |
| `disabled_by`                                                        | [models.DisabledBy](../models/disabledby.md)                         | :heavy_check_mark:                                                   | Who disabled the flow (system or user)                               |