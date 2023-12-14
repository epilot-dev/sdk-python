# Internal
(*internal*)

### Available Operations

* [list_portals_internal](#list_portals_internal) - listPortalsInternal

## list_portals_internal

List all portals (internal API)

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.internal.list_portals_internal("<YOUR_BEARER_TOKEN_HERE>", fields=[
    'id',
    'name',
    'origin',
    'enabled',
    'domain',
], from_=0, size=25)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.ListPortalsInternalSecurity](../../models/operations/listportalsinternalsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |                                                                                                  |
| `fields`                                                                                         | List[*str*]                                                                                      | :heavy_minus_sign:                                                                               | N/A                                                                                              | ["id","name","origin","enabled","domain"]                                                        |
| `from_`                                                                                          | *Optional[float]*                                                                                | :heavy_minus_sign:                                                                               | N/A                                                                                              | 0                                                                                                |
| `size`                                                                                           | *Optional[float]*                                                                                | :heavy_minus_sign:                                                                               | N/A                                                                                              | 25                                                                                               |


### Response

**[operations.ListPortalsInternalResponse](../../models/operations/listportalsinternalresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
