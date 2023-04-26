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
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.AssignThreadRequest(
    request_body=[
        operations.AssignThreadRequestBody(
            entity_id="3f34ce73-089c-4d45-a5ee-c161234e41c3",
            is_main_entity=True,
            slug="contact",
        ),
        operations.AssignThreadRequestBody(
            entity_id="3f34ce73-089c-4d45-a5ee-c161234e41c3",
            is_main_entity=True,
            slug="contact",
        ),
        operations.AssignThreadRequestBody(
            entity_id="3f34ce73-089c-4d45-a5ee-c161234e41c3",
            is_main_entity=True,
            slug="contact",
        ),
        operations.AssignThreadRequestBody(
            entity_id="3f34ce73-089c-4d45-a5ee-c161234e41c3",
            is_main_entity=True,
            slug="contact",
        ),
    ],
    id="9cbf4863-3323-4f9b-b7f3-a4100674ebf6",
)

res = s.threads.assign_thread(req)

if res.status_code == 200:
    # handle response
```

## delete_thread

Immediately and permanently delete a thread. This operation cannot be undone.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DeleteThreadRequest(
    id="9280d1ba-77a8-49eb-b737-ae4203ce5e6a",
)

res = s.threads.delete_thread(req)

if res.status_code == 200:
    # handle response
```

## mark_read_thread

Mark thread as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.MarkReadThreadRequest(
    id="95d8a0d4-46ce-42af-ba73-cf3be453f870",
)

res = s.threads.mark_read_thread(req)

if res.status_code == 200:
    # handle response
```

## mark_unread_thread

Mark thread as unread

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.MarkUnreadThreadRequest(
    id="b326b5a7-3429-4cdb-9a84-22bb679d2322",
)

res = s.threads.mark_unread_thread(req)

if res.status_code == 200:
    # handle response
```

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
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.SearchParams(
    from_=488056,
    q="subject:"Request for solar panel price" AND _tags:INBOX",
    size=124833,
)

res = s.threads.search_threads(req)

if res.search_threads_200_application_json_object is not None:
    # handle response
```

## trash_thread

Move a thread to trash

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.TrashThreadRequest(
    id="5bf0cbb1-e31b-48b9-8f34-43a1108e0adc",
)

res = s.threads.trash_thread(req)

if res.status_code == 200:
    # handle response
```

## untrash_thread

Restore a trashed thread

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UntrashThreadRequest(
    id="f4b92187-9fce-4953-b73e-f7fbc7abd74d",
)

res = s.threads.untrash_thread(req)

if res.status_code == 200:
    # handle response
```

## update_thread

Modify thread metadata

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.threads.update_thread()

if res.update_thread_201_application_json_object is not None:
    # handle response
```
