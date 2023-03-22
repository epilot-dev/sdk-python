<div align="center">
    <picture>
        <source srcset="https://user-images.githubusercontent.com/68016351/221740028-fbe0a2da-c781-4641-ac18-0bb1d19d49e3.svg" media="(prefers-color-scheme: dark)" width="500">
        <img src="https://user-images.githubusercontent.com/68016351/221764522-4c54cadc-7697-49cf-a4f2-2838a8b30796.png" width="500">
    </picture>
   <p>Epilot is the digital foundation for sales, service, network and implementation processes in the context of the energy transition..</p>
   <a href="https://docs.epilot.io/api/access-token"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

This is a monorepo of Python SDKs for the Epilot APIs. Please see the Epilot [developer documentation](https://docs.epilot.io/docs/intro/) for more information. Each SDK is an independent package with the folder name representing the API.

## SDK Installation

SDKs for each API are independently versioned and tagged enabling a per API installation. For example the sdk for the Automation API can be installed as follows: 

```bash
pip install epilot-automation
```

## Authentication

To call epilot APIs, requests must be authorized using a valid Access Token.

### Using Access Token Authorization
The access token should be passed in the Authorization request header.

```bash
Authorization: Bearer <your-access-token>
```

### Creating Access Tokens
Users logged into the epilot 360 portal can manage their Access Tokens from Settings > Access Tokens.

Creating access tokens requires the `token:create` permission.

Access Token API
Authenticated users can generate long-term access tokens for 3rd party applications using the epilot Access Token API createAccessToken operation.

```bash
POST /v1/access-tokens
{
  "name": "Token for my application"
}
```
Optionally, you can pass a list of Role IDs, to define the roles the access token will have access to. By default, the access token inherits the caller's roles.

```bash
POST /v1/access-tokens
{
  "name": "Postman Access Token",
  "assume_roles": ["123:owner"]
}
```
Each Access Token generated via the API gets a generated a unique ID.

```bash
// 201 - success
{
  "id": "api_5ZugdRXasLfWBypHi93Fk",
  "created_at": "2019-08-24T14:15:22Z",
  "name": "Postman Access Token",
  "assignments": ["123:owner"]
}
```
Access tokens may also be revoked using the revokeAccessToken operation
```bash
DELETE /v1/access-tokens/api_5ZugdRXasLfWBypHi93Fk
// 200 - success
{
  "id": "api_5ZugdRXasLfWBypHi93Fk",
  "created_at": "2019-08-24T14:15:22Z",
  "name": "Postman Access Token",
  "assignments": ["123:owner"]
}
```
## SDK Example Usage

Here is an example of using the SDK. Please refer to each sub SDK folder for usage examples specific to an API. 

<!-- Start SDK Example Usage -->
```python
```
<!-- End SDK Example Usage -->

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
