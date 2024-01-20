# epilot-file

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=file
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [files](docs/sdks/files/README.md)

* [access_public_link](docs/sdks/files/README.md#access_public_link) - accessPublicLink
* [delete_file](docs/sdks/files/README.md#delete_file) - deleteFile
* [download_file](docs/sdks/files/README.md#download_file) - downloadFile
* [download_files](docs/sdks/files/README.md#download_files) - downloadFiles
* [download_s3_file](docs/sdks/files/README.md#download_s3_file) - downloadS3File
* [generate_public_link](docs/sdks/files/README.md#generate_public_link) - generatePublicLink
* [get_all_public_links_for_file](docs/sdks/files/README.md#get_all_public_links_for_file) - getAllPublicLinksForFile
* [preview_file](docs/sdks/files/README.md#preview_file) - previewFile
* [preview_public_file](docs/sdks/files/README.md#preview_public_file) - previewPublicFile
* [preview_s3_file](docs/sdks/files/README.md#preview_s3_file) - previewS3File
* [preview_s3_file_get](docs/sdks/files/README.md#preview_s3_file_get) - previewS3FileGet
* [revoke_public_link](docs/sdks/files/README.md#revoke_public_link) - revokePublicLink
* [save_file](docs/sdks/files/README.md#save_file) - saveFile
* [upload_file](docs/sdks/files/README.md#upload_file) - uploadFile
* [upload_file_public](docs/sdks/files/README.md#upload_file_public) - uploadFilePublic
* [upload_file_v2](docs/sdks/files/README.md#upload_file_v2) - uploadFileV2
* [verify_custom_download_url](docs/sdks/files/README.md#verify_custom_download_url) - verifyCustomDownloadUrl

### [session](docs/sdks/session/README.md)

* [delete_session](docs/sdks/session/README.md#delete_session) - deleteSession
* [get_session](docs/sdks/session/README.md#get_session) - getSession
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = None
try:
    res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://file.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    server_idx=0,
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    server_url="https://file.sls.epilot.io",
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `cookie_auth` | apiKey        | API key       |
| `epilot_auth` | http          | HTTP Bearer   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
