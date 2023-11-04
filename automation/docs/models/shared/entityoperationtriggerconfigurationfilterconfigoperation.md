# EntityOperationTriggerConfigurationFilterConfigOperation


## Fields

| Field                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `diff`                                                                                                                                                                                                                                                                  | [Optional[Union[OrConditionForDiff, EntityOperationTriggerConfigurationFilterConfigOperationDiff2]]](../../models/shared/entityoperationtriggerconfigurationfilterconfigoperationdiff.md)                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                     |
| `operation`                                                                                                                                                                                                                                                             | List[[EntityOperation](../../models/shared/entityoperation.md)]                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Filter on operation type. If not specified, all operations will be matched on execution.<br/>Example:<br/>  1. Filter all the createEntity/updateEntity operations <br/>  ```<br/>    { <br/>      "operation":{<br/>        "operation": ["createEntity", "updateEntity"]<br/>      }<br/>    }<br/>  ```<br/> |
| `payload`                                                                                                                                                                                                                                                               | [Optional[Union[OrCondition1, Dict[str, List[Union[str, EqualsIgnoreCaseCondition, AnythingButCondition, NumericCondition, ExistsCondition, PrefixCondition, SuffixCondition]]]]]](../../models/shared/filterconditiononevent.md)                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                     |