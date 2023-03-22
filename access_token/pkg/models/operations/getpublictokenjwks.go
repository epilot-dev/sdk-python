// Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.

package operations

import (
	"net/http"
)

type GetPublicTokenJwks200ApplicationJSONKeys struct {
	Alg *string `json:"alg,omitempty"`
	E   *string `json:"e,omitempty"`
	Kid *string `json:"kid,omitempty"`
	Kty *string `json:"kty,omitempty"`
	N   *string `json:"n,omitempty"`
	Use *string `json:"use,omitempty"`
}

// GetPublicTokenJwks200ApplicationJSON - Set of jwks
type GetPublicTokenJwks200ApplicationJSON struct {
	Keys []GetPublicTokenJwks200ApplicationJSONKeys `json:"keys,omitempty"`
}

type GetPublicTokenJwksResponse struct {
	ContentType string
	StatusCode  int
	RawResponse *http.Response
	// Set of jwks
	GetPublicTokenJwks200ApplicationJSONObject *GetPublicTokenJwks200ApplicationJSON
}
