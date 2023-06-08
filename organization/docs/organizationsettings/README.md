# organization_settings

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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteSettingsValueRequest(
    key='veritatis',
    org_id='739224',
)

res = s.organization_settings.delete_settings_value(req)

if res.status_code == 200:
    # handle response
```

## get_settings

Get full organization settings object

### Example Usage

```python
import epilot
from epilot.models import operations

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

## put_settings_value

Updates an organization setting

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PutSettingsValueRequest(
    request_body=[
        {
            "repellendus": 'sapiente',
            "quo": 'odit',
        },
    ],
    key='at',
    org_id='739224',
)

res = s.organization_settings.put_settings_value(req)

if res.settings_value is not None:
    # handle response
```
