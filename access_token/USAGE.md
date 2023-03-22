<!-- Start SDK Example Usage -->
```go
package main

import (
    "context"
    "log"
    "openapi"
    "openapi/pkg/models/shared"
    "openapi/pkg/models/operations"
)

func main() {
    s := epilot.New(
        epilot.WithSecurity(shared.Security{
            EpilotAuth: epilot.String("Bearer YOUR_BEARER_TOKEN_HERE"),
        }),
    )

    req := interface{}{}

    ctx := context.Background()
    res, err := s.AccessTokens.CreateAccessToken(ctx, req)
    if err != nil {
        log.Fatal(err)
    }

    if res.CreateAccessToken201ApplicationJSONObject != nil {
        // handle response
    }
}
```
<!-- End SDK Example Usage -->