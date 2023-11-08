# UserExistsResponseBody

Returned whether the user exists in the portal or not successfully.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `exists`                                                             | *bool*                                                               | :heavy_check_mark:                                                   | Whether the user exists in the portal                                | true                                                                 |
| `user`                                                               | [Optional[components.PortalUser]](../../models/shared/portaluser.md) | :heavy_minus_sign:                                                   | The portal user entity                                               |                                                                      |