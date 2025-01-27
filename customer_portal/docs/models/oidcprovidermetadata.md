# OIDCProviderMetadata


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `authorization_endpoint`                            | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL of the authorization endpoint                   | https://www.facebook.com/v12.0/dialog/oauth         |
| `token_endpoint`                                    | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL of the token endpoint                           | https://graph.facebook.com/v12.0/oauth/access_token |
| `userinfo_endpoint`                                 | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL of the userinfo endpoint                        | https://graph.facebook.com/me                       |