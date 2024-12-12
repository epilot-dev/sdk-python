# Threads
(*threads*)

## Overview

### Available Operations

* [assign_thread](#assign_thread) - assignThread
* [assign_users](#assign_users) - assignUsers
* [delete_thread](#delete_thread) - deleteThread
* [mark_read_thread](#mark_read_thread) - markReadThread
* [mark_read_thread_v2](#mark_read_thread_v2) - markReadThreadV2
* [mark_unread_thread](#mark_unread_thread) - markUnreadThread
* [mark_unread_thread_v2](#mark_unread_thread_v2) - markUnreadThreadV2
* [search_threads](#search_threads) - searchThreads
* [trash_thread](#trash_thread) - trashThread
* [unassign_thread](#unassign_thread) - unassignThread
* [untrash_thread](#untrash_thread) - untrashThread
* [update_thread](#update_thread) - updateThread

## assign_thread

Assign thread to entities

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.assign_thread(id="<id>", request_body=[
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## assign_users

Assign users to thread for receiving notifications.
The operation replaces all existing assigned users in thread.


### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.assign_users(id="<id>", request_body={
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_thread

Immediately and permanently delete a thread. This operation cannot be undone.

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.delete_thread(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## mark_read_thread

Mark thread as read

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.mark_read_thread(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## mark_read_thread_v2

Mark thread as read within a scope

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.mark_read_thread_v2(id="<id>", read_message_payload={
        "scopes": [
            epilot_message.ReadingScope.ORGANIZATION,
            epilot_message.ReadingScope.USER,
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `read_message_payload`                                              | [models.ReadMessagePayload](../../models/readmessagepayload.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## mark_unread_thread

Mark thread as unread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.mark_unread_thread(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## mark_unread_thread_v2

Mark thread as unread within a scope

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.mark_unread_thread_v2(id="<id>", read_message_payload={
        "scopes": [
            epilot_message.ReadingScope.ORGANIZATION,
            epilot_message.ReadingScope.USER,
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `read_message_payload`                                              | [models.ReadMessagePayload](../../models/readmessagepayload.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## search_threads

Search for threads of email messages.

Messages with no replies yet are treated as threads with single message.

Lucene syntax supported.


### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.threads.search_threads(request={
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## trash_thread

Move a thread to trash

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.trash_thread(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## unassign_thread

Unassign thread from entities

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.unassign_thread(id="<id>", request_body=[
        {
            "entity_id": "3f34ce73-089c-4d45-a5ee-c161234e41c3",
            "slug": "contact",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | Thread ID                                                                           |
| `request_body`                                                                      | List[[models.UnassignThreadRequestBody](../../models/unassignthreadrequestbody.md)] | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## untrash_thread

Restore a trashed thread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.threads.untrash_thread(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_thread

Modify thread metadata

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

with Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.threads.update_thread()

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |