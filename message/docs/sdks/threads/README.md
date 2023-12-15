# Threads
(*threads*)

### Available Operations

* [assign_thread](#assign_thread) - assignThread
* [assign_users](#assign_users) - assignUsers
* [delete_thread](#delete_thread) - deleteThread
* [mark_read_thread](#mark_read_thread) - markReadThread
* [mark_unread_thread](#mark_unread_thread) - markUnreadThread
* [search_threads](#search_threads) - searchThreads
* [trash_thread](#trash_thread) - trashThread
* [untrash_thread](#untrash_thread) - untrashThread
* [update_thread](#update_thread) - updateThread

## assign_thread

Assign thread to entities

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.assign_thread(request_body=[
    operations.RequestBody(
        entity_id='3f34ce73-089c-4d45-a5ee-c161234e41c3',
        is_main_entity=True,
        slug='contact',
    ),
], id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request_body`                                                         | List[[operations.RequestBody](../../models/operations/requestbody.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Thread ID                                                              |


### Response

**[operations.AssignThreadResponse](../../models/operations/assignthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## assign_users

Assign users to thread for receiving notifications. 
The operation replaces all existing assigned users in thread.


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.assign_users(request_body=operations.AssignUsersRequestBody(
    assigned_to=[
        '206801',
    ],
), id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request_body`                                                                         | [operations.AssignUsersRequestBody](../../models/operations/assignusersrequestbody.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Thread ID                                                                              |


### Response

**[operations.AssignUsersResponse](../../models/operations/assignusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_thread

Immediately and permanently delete a thread. This operation cannot be undone.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.delete_thread(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Thread ID          |


### Response

**[operations.DeleteThreadResponse](../../models/operations/deletethreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## mark_read_thread

Mark thread as read

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.mark_read_thread(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Thread ID          |


### Response

**[operations.MarkReadThreadResponse](../../models/operations/markreadthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## mark_unread_thread

Mark thread as unread

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.mark_unread_thread(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Thread ID          |


### Response

**[operations.MarkUnreadThreadResponse](../../models/operations/markunreadthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## search_threads

Search for threads of email messages.

Messages with no replies yet are treated as threads with single message.

Lucene syntax supported.


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.SearchParams(
    q='subject:"Request for solar panel price" AND _tags:INBOX',
)

res = s.threads.search_threads(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.SearchParams](../../models/components/searchparams.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.SearchThreadsResponse](../../models/operations/searchthreadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## trash_thread

Move a thread to trash

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.trash_thread(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Thread ID          |


### Response

**[operations.TrashThreadResponse](../../models/operations/trashthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## untrash_thread

Restore a trashed thread

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.untrash_thread(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Thread ID          |


### Response

**[operations.UntrashThreadResponse](../../models/operations/untrashthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_thread

Modify thread metadata

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.update_thread()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateThreadResponse](../../models/operations/updatethreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
