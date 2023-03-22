// Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.

package shared

type AccessTokenParametersTokenTypeEnum string

const (
	AccessTokenParametersTokenTypeEnumAPI AccessTokenParametersTokenTypeEnum = "api"
)

type AccessTokenParameters struct {
	// List of role ids attached to an user
	Assignments []string `json:"assignments,omitempty"`
	// Human readable name for access token
	Name      string                              `json:"name"`
	TokenType *AccessTokenParametersTokenTypeEnum `json:"token_type,omitempty"`
}
