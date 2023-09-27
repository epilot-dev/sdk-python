# SavedViews
(*saved_views*)

## Overview

Saved Views for Entities

### Available Operations

* [create_saved_view](#create_saved_view) - createSavedView
* [delete_saved_view](#delete_saved_view) - deleteSavedView
* [get_saved_view](#get_saved_view) - getSavedView
* [list_favorite_views_for_user](#list_favorite_views_for_user) - listFavoriteViewsForUser
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
        epilot_auth="",
    ),
)

req = shared.SavedView(
    created_by=[],
    is_favorited_by=[
        '11701',
    ],
    name='View listing German',
    org='66',
    shared=True,
    slug=[
        'contact',
    ],
    ui_config={
        "voluptatem": 'cumque',
    },
)

res = s.saved_views.create_saved_view(req)

if res.saved_view_item is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.SavedView](../../models/shared/savedview.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.CreateSavedViewResponse](../../models/operations/createsavedviewresponse.md)**


## delete_saved_view

Deletes a saved view

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteSavedViewRequest(
    id='bb1e31b8-b90f-4344-ba11-08e0adcf4b92',
)

res = s.saved_views.delete_saved_view(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteSavedViewRequest](../../models/operations/deletesavedviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeleteSavedViewResponse](../../models/operations/deletesavedviewresponse.md)**


## get_saved_view

Gets Saved View configuration by id.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSavedViewRequest(
    id='1879fce9-53f7-43ef-bfbc-7abd74dd39c0',
)

res = s.saved_views.get_saved_view(req)

if res.get_saved_view_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetSavedViewRequest](../../models/operations/getsavedviewrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetSavedViewResponse](../../models/operations/getsavedviewresponse.md)**


## list_favorite_views_for_user

Get the Favorite Saved Views for user based on the schema

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.list_favorite_views_for_user()

if res.list_favorite_views_for_user_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListFavoriteViewsForUserResponse](../../models/operations/listfavoriteviewsforuserresponse.md)**


## list_saved_views

Get the Saved Views based on the schema

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.list_saved_views()

if res.list_saved_views_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListSavedViewsResponse](../../models/operations/listsavedviewsresponse.md)**


## update_saved_view

Updates a saved view

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateSavedViewRequest(
    saved_view=shared.SavedView(
        created_by=[],
        is_favorited_by=[
            '11701',
        ],
        name='View listing German',
        org='66',
        shared=True,
        slug=[
            'contact',
        ],
        ui_config={
            "voluptatibus": 'exercitationem',
        },
    ),
    id='d2cff7c7-0a45-4626-9436-813f16d9f5fc',
)

res = s.saved_views.update_saved_view(req)

if res.saved_view_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateSavedViewRequest](../../models/operations/updatesavedviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateSavedViewResponse](../../models/operations/updatesavedviewresponse.md)**

