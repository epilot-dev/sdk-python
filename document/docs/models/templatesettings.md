# TemplateSettings

Template Settings for document generation


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `custom_margins`                                                                      | [Optional[models.CustomMargins]](../models/custommargins.md)                          | :heavy_minus_sign:                                                                    | Custom margins for the document                                                       |                                                                                       |
| `display_margin_guidelines`                                                           | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Display margin guidelines (applicable to partial generation only)                     | true                                                                                  |
| `enable_data_table_margin_autofix`                                                    | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Enable data table margin autofix                                                      | false                                                                                 |
| `enabled_template_settings_persistence`                                               | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Enables the persistance of template settings                                          | false                                                                                 |
| `file_entity_id`                                                                      | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | The file entity id, used when persisting a new template version with updated settings | 1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p                                                  |
| `misconfigured_margins`                                                               | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | An indication that the page margins are misconfigured                                 | false                                                                                 |
| `suggested_margins`                                                                   | [Optional[models.SuggestedMargins]](../models/suggestedmargins.md)                    | :heavy_minus_sign:                                                                    | Suggested margins for the document                                                    |                                                                                       |
| `template_with_datatable`                                                             | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | A flag that indicates whether the template has 1 or more data tables in it            | false                                                                                 |