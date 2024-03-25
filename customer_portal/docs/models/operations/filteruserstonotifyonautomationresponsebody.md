# FilterUsersToNotifyOnAutomationResponseBody

Returned whether the user exists in the portal or not successfully.


## Fields

| Field                         | Type                          | Required                      | Description                   | Example                       |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `emails`                      | List[*str*]                   | :heavy_check_mark:            | Filtered emails on a portal   | [<br/>"john@doe.com"<br/>]    |
| `message`                     | *Optional[str]*               | :heavy_minus_sign:            | Reason to not notify the user |                               |