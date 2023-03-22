// Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.

package operations

import (
	"net/http"
	"openapi/pkg/models/shared"
)

type RevokeAccessTokenRequest struct {
	ID string `pathParam:"style=simple,explode=false,name=id"`
}

type RevokeAccessTokenResponse struct {
	// The revoked generated Access Token
	AccessTokenItem *shared.AccessTokenItem
	ContentType     string
	StatusCode      int
	RawResponse     *http.Response
}
