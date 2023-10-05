# OrganizationSettings
(*organization_settings*)

## Overview

Organisation Settings

### Available Operations

* [delete_settings_value](#delete_settings_value) - deleteSettingsValue
* [get_settings](#get_settings) - getSettings
* [put_settings_value](#put_settings_value) - putSettingsValue

## delete_settings_value

Updates an organizatio nsetting

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteSettingsValueRequest(
    key='<key>',
    org_id='739224',
)

res = s.organization_settings.delete_settings_value(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteSettingsValueRequest](../../models/operations/deletesettingsvaluerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DeleteSettingsValueResponse](../../models/operations/deletesettingsvalueresponse.md)**


## get_settings

Get full organization settings object

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSettingsRequest(
    org_id='739224',
)

res = s.organization_settings.get_settings(req)

if res.settings is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSettingsRequest](../../models/operations/getsettingsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetSettingsResponse](../../models/operations/getsettingsresponse.md)**


## put_settings_value

Updates an organization setting

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PutSettingsValueRequest(
    settings_value=[],
    key='<key>',
    org_id='739224',
)

res = s.organization_settings.put_settings_value(req)

if res.settings_value is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PutSettingsValueRequest](../../models/operations/putsettingsvaluerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PutSettingsValueResponse](../../models/operations/putsettingsvalueresponse.md)**

