# LoginToPortalAsUserRequestBody

The request body to log in to a portal impersonating a user


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `email`                                        | *Optional[str]*                                | :heavy_minus_sign:                             | The email address of the user to log in as     | portal-customer@email.com                      |
| `origin`                                       | [Optional[models.Origin]](../models/origin.md) | :heavy_minus_sign:                             | Origin of the portal                           |                                                |