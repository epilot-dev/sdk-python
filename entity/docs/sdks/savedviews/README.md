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
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)

req = components.SavedView(
    created_by=components.SavedView1(
    user_id='10598',
),
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
        "filters": 'string',
        "table_layout": 'string',
    },
)

res = s.saved_views.create_saved_view(req)

if res.saved_view_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.SavedView](../../models/components/savedview.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateSavedViewResponse](../../models/operations/createsavedviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_saved_view

Deletes a saved view

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.delete_saved_view(id='59eccd11-7c56-46ef-bb90-41cbc04178cc')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | View id            |


### Response

**[operations.DeleteSavedViewResponse](../../models/operations/deletesavedviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_saved_view

Gets Saved View configuration by id.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.get_saved_view(id='638188cd-8a1e-442e-95b2-8864469eafc5')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | View id            |


### Response

**[operations.GetSavedViewResponse](../../models/operations/getsavedviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_favorite_views_for_user

Get the Favorite Saved Views for user based on the schema

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.list_favorite_views_for_user()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.ListFavoriteViewsForUserResponse](../../models/operations/listfavoriteviewsforuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_saved_views

Get the Saved Views based on the schema

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.list_saved_views(slug='contact')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `slug`                                | *Optional[str]*                       | :heavy_minus_sign:                    | Return views belonging to this schema | contact                               |


### Response

**[operations.ListSavedViewsResponse](../../models/operations/listsavedviewsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_saved_view

Updates a saved view

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.saved_views.update_saved_view(id='0203092c-d478-4166-8df5-5b0841d72e4e', saved_view=components.SavedView(
    created_by=components.SavedView1(
    user_id='10598',
),
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
        "filters": 'string',
        "table_layout": 'string',
    },
))

if res.saved_view_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | View id                                                                |
| `saved_view`                                                           | [Optional[components.SavedView]](../../models/components/savedview.md) | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.UpdateSavedViewResponse](../../models/operations/updatesavedviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
