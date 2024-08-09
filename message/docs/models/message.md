# Message


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                                           | [models.Address](../models/address.md)                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `subject`                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                | Subject                                                                                                                                                                                                                                                                                                                                                                                                           | Request for solar panel price                                                                                                                                                                                                                                                                                                                                                                                     |
| `bcc`                                                                                                                                                                                                                                                                                                                                                                                                             | List[[models.Address](../models/address.md)]                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Bcc email addresses                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `cc`                                                                                                                                                                                                                                                                                                                                                                                                              | List[[models.Address](../models/address.md)]                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Cc email addresses                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `file`                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.AttachmentsRelation]](../models/attachmentsrelation.md)                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Message attachments                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `html`                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | HTML body                                                                                                                                                                                                                                                                                                                                                                                                         | <div>We at ABC GmbH would like to request a price quote for the solar panel.</div>                                                                                                                                                                                                                                                                                                                                |
| `in_reply_to`                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | In-Reply-To header. Value is the `message_id` of parent message.<br/>                                                                                                                                                                                                                                                                                                                                             | <CALHgQpziyxW9NaFUs+nRMykzr6Ljq6vjq4WO9SaihAuMasuDyg@mail.gmail.com>                                                                                                                                                                                                                                                                                                                                              |
| `message_id`                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Message ID which is from email provider. If you provide `message-id`, API overrides by its own value.                                                                                                                                                                                                                                                                                                             | <0102017b97a502f8-a67f01c2-68cc-4928-b91b-45853f34e259-000000@eu-west-1.amazonses.com>                                                                                                                                                                                                                                                                                                                            |
| `org_read_message`                                                                                                                                                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Ivy Organization ID of organization read the message.                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `references`                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | References header. Value is the series of `message_id` which is reparated by space to indicate that message has parent.            The last message ID in references identifies the parent. The first message ID in references identifies the first message in the thread.            The basic idea is that sender should copy `references` from the parent and append the parent's `message_id` when replying.<br/> | <0102017b97a502f8-a67f01c2-68cc-4928-b91b-45853f34e259-000000@eu-west-1.amazonses.com> <CALHgQpziyxW9NaFUs+nRMykzr6Ljq6vjq4WO9SaihAuMasuDyg@mail.gmail.com>                                                                                                                                                                                                                                                       |
| `reply_to`                                                                                                                                                                                                                                                                                                                                                                                                        | [Optional[models.Address]](../models/address.md)                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `send_status`                                                                                                                                                                                                                                                                                                                                                                                                     | List[[models.MessageSendStatus](../models/messagesendstatus.md)]                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Sent message status. The array contains sending message status corresponding to all recipients. For more detail, check `send_status` of each recipient in `to`, `cc`, `bcc`            Reference at <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html><br/>                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sender`                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Ivy User ID of user sends the message.                                                                                                                                                                                                                                                                                                                                                                            | 206801                                                                                                                                                                                                                                                                                                                                                                                                            |
| `text`                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Text body                                                                                                                                                                                                                                                                                                                                                                                                         | We at ABC GmbH would like to request a price quote for the solar panel.                                                                                                                                                                                                                                                                                                                                           |
| `to`                                                                                                                                                                                                                                                                                                                                                                                                              | List[[models.Address](../models/address.md)]                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | To email addresses                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `type`                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.Type]](../models/type.md)                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Message type                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `user_read_message`                                                                                                                                                                                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                | Ivy User ID of user read the message.                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                   |