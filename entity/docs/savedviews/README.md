# saved_views

## Overview

Saved Views for Entities

### Available Operations

* [create_saved_view](#create_saved_view) - createSavedView
* [delete_saved_view](#delete_saved_view) - deleteSavedView
* [get_saved_view](#get_saved_view) - getSavedView
* [list_saved_views](#list_saved_views) - listSavedViews
* [update_saved_view](#update_saved_view) - updateSavedView

## create_saved_view

Creates a new saved view

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.SavedView(
    created_by=shared.SavedViewCreatedBy1(
        user_id='10598',
    ),
    name='View listing German',
    org='66',
    shared=True,
    slug=[
        'contact',
        'contact',
    ],
    ui_config={
        "cupiditate": 'consequatur',
    },
)

res = s.saved_views.create_saved_view(req)

if res.saved_view_item is not None:
    # handle response
```

## delete_saved_view

Deletes a saved view

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DeleteSavedViewRequest(
    id='4e523c7e-0bc7-4178-a479-6f2a70c68828',
)

res = s.saved_views.delete_saved_view(req)

if res.status_code == 200:
    # handle response
```

## get_saved_view

Gets Saved View configuration by id.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetSavedViewRequest(
    id='2aa48256-2f22-42e9-817e-e17cbe61e6b7',
)

res = s.saved_views.get_saved_view(req)

if res.get_saved_view_200_application_json_object is not None:
    # handle response
```

## list_saved_views

Get the Saved Views based on the schema

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.saved_views.list_saved_views()

if res.list_saved_views_200_application_json_object is not None:
    # handle response
```

## update_saved_view

Updates a saved view

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdateSavedViewRequest(
    saved_view=shared.SavedView(
        created_by={
            "minima": 'distinctio',
            "eligendi": 'sit',
            "culpa": 'tempore',
        },
        name='View listing German',
        org='66',
        shared=True,
        slug=[
            'contact',
        ],
        ui_config={
            "consequuntur": 'consequatur',
            "minus": 'quaerat',
            "sapiente": 'consectetur',
            "esse": 'blanditiis',
        },
    ),
    id='9fd871f9-9dd2-4efd-921a-a6f1e674bdb0',
)

res = s.saved_views.update_saved_view(req)

if res.saved_view_item is not None:
    # handle response
```
