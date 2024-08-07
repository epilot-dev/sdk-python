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
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.assign_thread(id="<value>", request_body=[
    {
        "entity_id": "3f34ce73-089c-4d45-a5ee-c161234e41c3",
        "is_main_entity": True,
        "slug": "contact",
    },
])

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `request_body`                                                      | List[[models.RequestBody](../../models/requestbody.md)]             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## assign_users

Assign users to thread for receiving notifications.
The operation replaces all existing assigned users in thread.


### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.assign_users(id="<value>", request_body={
    "assigned_to": [
        "206801",
    ],
})

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | Thread ID                                                               |
| `request_body`                                                          | [models.AssignUsersRequestBody](../../models/assignusersrequestbody.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_thread

Immediately and permanently delete a thread. This operation cannot be undone.

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.delete_thread(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## mark_read_thread

Mark thread as read

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.mark_read_thread(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## mark_unread_thread

Mark thread as unread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.mark_unread_thread(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_threads

Search for threads of email messages.

Messages with no replies yet are treated as threads with single message.

Lucene syntax supported.


### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.search_threads(request={
    "q": "subject:\"Request for solar panel price\" AND _tags:INBOX",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchParams](../../models/searchparams.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchThreadsResponseBody](../../models/searchthreadsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## trash_thread

Move a thread to trash

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.trash_thread(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## untrash_thread

Restore a trashed thread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.threads.untrash_thread(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_thread

Modify thread metadata

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.threads.update_thread()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UpdateThreadResponseBody](../../models/updatethreadresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
