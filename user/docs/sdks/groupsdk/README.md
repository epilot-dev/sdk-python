# GroupSDK
(*group*)

## Overview

User Groups

### Available Operations

* [advance_user_assignment](#advance_user_assignment) - advanceUserAssignment
* [create_group](#create_group) - createGroup
* [delete_group](#delete_group) - deleteGroup
* [get_group](#get_group) - getGroup
* [get_groups](#get_groups) - getGroups
* [update_group](#update_group) - updateGroup

## advance_user_assignment

Advance user assignment to next user in line

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.advance_user_assignment(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group id                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Group](../../models/group.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create_group

Create a new group

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.create_group(request={
    "name": "Finance",
    "user_ids": [
        "123",
        "456",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateGroupReq](../../models/creategroupreq.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Group](../../models/group.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## delete_group

Delete group by id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.group.delete_group(id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group id                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## get_group

Get group by id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.get_group(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Group id                                                               |
| `hydrate`                                                              | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Pass it true when you want to hydrate the group with full user details |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.Group](../../models/group.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## get_groups

Lists groups in organizations you have access to

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.get_groups()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `hydrate`                                                              | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Pass it true when you want to hydrate the group with full user details |
| `limit`                                                                | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Limit the results size                                                 |
| `offset`                                                               | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Specify the offset                                                     |
| `query`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Query name to filter by                                                |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.GetGroupsResponseBody](../../models/getgroupsresponsebody.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## update_group

Update group by id

### Example Usage

```python
from epilot_user import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group.update_group(id="<id>", update_group_req={
    "name": "Finance",
    "user_ids": [
        "123",
        "456",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group id                                                            |
| `update_group_req`                                                  | [Optional[models.UpdateGroupReq]](../../models/updategroupreq.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Group](../../models/group.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
