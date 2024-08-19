# GetRecipientsToNotifyOnAutomationResponseBody

Returns the valid recipients to notify successfully.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `message`                                          | *Optional[str]*                                    | :heavy_minus_sign:                                 | Reason to not notify the user                      |
| `recipients`                                       | List[[models.Recipients](../models/recipients.md)] | :heavy_minus_sign:                                 | Filtered recipients to notify                      |