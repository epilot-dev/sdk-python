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
    epilot_auth="",
)


res = s.organization_settings.delete_settings_value(key='string', org_id='739224')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 | Example                     |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `key`                       | *str*                       | :heavy_check_mark:          | Organization setting key    |                             |
| `org_id`                    | *str*                       | :heavy_check_mark:          | The Id of the organization. | 739224                      |


### Response

**[operations.DeleteSettingsValueResponse](../../models/operations/deletesettingsvalueresponse.md)**


## get_settings

Get full organization settings object

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.organization_settings.get_settings(org_id='739224')

if res.settings is not None:
    # handle response
    pass
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 | Example                     |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `org_id`                    | *str*                       | :heavy_check_mark:          | The Id of the organization. | 739224                      |


### Response

**[operations.GetSettingsResponse](../../models/operations/getsettingsresponse.md)**


## put_settings_value

Updates an organization setting

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.organization_settings.put_settings_value(key='string', org_id='739224', settings_value={
    "enabled": 'string',
})

if res.settings_value is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     | Example                                                                                                         |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                           | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Organization setting key                                                                                        |                                                                                                                 |
| `org_id`                                                                                                        | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The Id of the organization.                                                                                     | 739224                                                                                                          |
| `settings_value`                                                                                                | [Optional[Union[str, float, bool, List[Dict[str, Any]], Dict[str, Any]]]](../../models/shared/settingsvalue.md) | :heavy_minus_sign:                                                                                              | Value to set                                                                                                    | [object Object]                                                                                                 |


### Response

**[operations.PutSettingsValueResponse](../../models/operations/putsettingsvalueresponse.md)**

