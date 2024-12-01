# CreateGroupReq


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `name`                                                  | *str*                                                   | :heavy_check_mark:                                      | The name of the group. Could be a department or a team. | Finance                                                 |
| `user_ids`                                              | List[*str*]                                             | :heavy_minus_sign:                                      | The list of user ids in the group.                      | [<br/>"123",<br/>"456"<br/>]                            |