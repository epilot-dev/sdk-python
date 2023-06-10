# threads

### Available Operations

* [assign_thread](#assign_thread) - assignThread
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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AssignThreadRequest(
    request_body=[
        operations.AssignThreadRequestBody(
            entity_id='3f34ce73-089c-4d45-a5ee-c161234e41c3',
            is_main_entity=True,
            slug='contact',
        ),
        operations.AssignThreadRequestBody(
            entity_id='3f34ce73-089c-4d45-a5ee-c161234e41c3',
            is_main_entity=True,
            slug='contact',
        ),
        operations.AssignThreadRequestBody(
            entity_id='3f34ce73-089c-4d45-a5ee-c161234e41c3',
            is_main_entity=True,
            slug='contact',
        ),
    ],
    id='8f3a6699-7074-4ba4-869b-6e2141959890',
)

res = s.threads.assign_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.AssignThreadRequest](../../models/operations/assignthreadrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.AssignThreadResponse](../../models/operations/assignthreadresponse.md)**


## delete_thread

Immediately and permanently delete a thread. This operation cannot be undone.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteThreadRequest(
    id='afa563e2-516f-4e4c-8b71-1e5b7fd2ed02',
)

res = s.threads.delete_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteThreadRequest](../../models/operations/deletethreadrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteThreadResponse](../../models/operations/deletethreadresponse.md)**


## mark_read_thread

Mark thread as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkReadThreadRequest(
    id='8921cddc-6926-401f-b576-b0d5f0d30c5f',
)

res = s.threads.mark_read_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.MarkReadThreadRequest](../../models/operations/markreadthreadrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.MarkReadThreadResponse](../../models/operations/markreadthreadresponse.md)**


## mark_unread_thread

Mark thread as unread

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkUnreadThreadRequest(
    id='bb258705-3202-4c73-95fe-9b90c28909b3',
)

res = s.threads.mark_unread_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.MarkUnreadThreadRequest](../../models/operations/markunreadthreadrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.MarkUnreadThreadResponse](../../models/operations/markunreadthreadresponse.md)**


## search_threads

Search for threads of email messages.

Messages with no replies yet are treated as threads with single message.

Lucene syntax supported.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.SearchParams(
    from_=992397,
    q='subject:"Request for solar panel price" AND _tags:INBOX',
    size=934214,
)

res = s.threads.search_threads(req)

if res.search_threads_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SearchParams](../../models/shared/searchparams.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.SearchThreadsResponse](../../models/operations/searchthreadsresponse.md)**


## trash_thread

Move a thread to trash

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.TrashThreadRequest(
    id='49a8d9cb-f486-4333-a3f9-b77f3a410067',
)

res = s.threads.trash_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.TrashThreadRequest](../../models/operations/trashthreadrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.TrashThreadResponse](../../models/operations/trashthreadresponse.md)**


## untrash_thread

Restore a trashed thread

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UntrashThreadRequest(
    id='4ebf6928-0d1b-4a77-a89e-bf737ae4203c',
)

res = s.threads.untrash_thread(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UntrashThreadRequest](../../models/operations/untrashthreadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UntrashThreadResponse](../../models/operations/untrashthreadresponse.md)**


## update_thread

Modify thread metadata

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.threads.update_thread()

if res.update_thread_201_application_json_object is not None:
    # handle response
```


### Response

**[operations.UpdateThreadResponse](../../models/operations/updatethreadresponse.md)**

