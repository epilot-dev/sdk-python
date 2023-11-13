# MappingAttributeV2


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `operation`                                                                            | [Union[components.OperationObjectNode, Any]](../../models/components/operationnode.md) | :heavy_check_mark:                                                                     | Mapping operation nodes are either primitive values or operation node objects          |
| `target`                                                                               | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Target JSON path for the attribute to set                                              |