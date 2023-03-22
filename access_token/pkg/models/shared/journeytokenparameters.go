// Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.

package shared

type JourneyTokenParametersTokenTypeEnum string

const (
	JourneyTokenParametersTokenTypeEnumJourney JourneyTokenParametersTokenTypeEnum = "journey"
)

type JourneyTokenParameters struct {
	// Journey ID for access token type "journey"
	JourneyID string `json:"journey_id"`
	// Human readable name for access token
	Name      string                               `json:"name"`
	TokenType *JourneyTokenParametersTokenTypeEnum `json:"token_type,omitempty"`
}
