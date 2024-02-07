# SectionSimplified

A group of Steps that define the progress of the Workflow


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name for this Section                                                | Lead Qualification                                                   |
| `steps`                                                              | List[[shared.StepSimplified](../../models/shared/stepsimplified.md)] | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `type`                                                               | [shared.ItemType](../../models/shared/itemtype.md)                   | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `definition_id`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |