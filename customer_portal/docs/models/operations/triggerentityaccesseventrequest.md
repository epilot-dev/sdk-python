# TriggerEntityAccessEventRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `origin`                                               | [components.Origin](../../models/components/origin.md) | :heavy_check_mark:                                     | Portal origin                                          |                                                        |
| `schema`                                               | *str*                                                  | :heavy_check_mark:                                     | Entity schema                                          | contract                                               |
| `entity_id`                                            | *Optional[str]*                                        | :heavy_minus_sign:                                     | Entity ID                                              | 1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e                   |