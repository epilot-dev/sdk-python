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
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.saved_views.create_saved_view(request={
    "created_by": {
        "user_id": "10598",
    },
    "name": "View listing German",
    "slug": [
        "contact",
    ],
    "ui_config": {
        "filters": {
            "customer_name": "suresh test",
            "_tags": "360",
        },
        "table_layout": {
            "opportunity": {
                "page": 1,
                "sort": "_created_at:desc",
                "pageSize": 25,
                "columnSettings": [
                    "<value>",
                ],
            },
        },
    },
    "is_favorited_by": [
        "11701",
    ],
    "org": "66",
    "shared": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SavedView](../../models/savedview.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SavedViewItem](../../models/savedviewitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_saved_view

Deletes a saved view

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.saved_views.delete_saved_view(request={
    "id": "59eccd11-7c56-46ef-bb90-41cbc04178cc",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.DeleteSavedViewRequest](../../models/deletesavedviewrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_saved_view

Gets Saved View configuration by id.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.saved_views.get_saved_view(request={
    "id": "638188cd-8a1e-442e-95b2-8864469eafc5",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetSavedViewRequest](../../models/getsavedviewrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SavedViewItem](../../models/savedviewitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_favorite_views_for_user

Get the Favorite Saved Views for user based on the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.saved_views.list_favorite_views_for_user()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListFavoriteViewsForUserResponseBody](../../models/listfavoriteviewsforuserresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_saved_views

Get the Saved Views based on the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.saved_views.list_saved_views(request={
    "fields": [
        "_id",
        "_title",
        "first_name",
        "account",
        "!account.*._files",
        "**._product",
    ],
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ListSavedViewsRequest](../../models/listsavedviewsrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.ListSavedViewsResults](../../models/listsavedviewsresults.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_saved_view

Updates a saved view

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.saved_views.update_saved_view(request={
    "id": "0203092c-d478-4166-8df5-5b0841d72e4e",
    "saved_view_item": {
        "created_by": {
            "user_id": "10598",
        },
        "name": "View listing German",
        "slug": [
            "contact",
        ],
        "ui_config": {
            "filters": {
                "customer_name": "suresh test",
                "_tags": "360",
            },
            "table_layout": {
                "opportunity": {
                    "page": 1,
                    "sort": "_created_at:desc",
                    "pageSize": 25,
                    "columnSettings": [
                        "<value>",
                    ],
                },
            },
        },
        "is_favorited_by": [
            "11701",
        ],
        "org": "66",
        "shared": True,
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UpdateSavedViewRequest](../../models/updatesavedviewrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |


### Response

**[models.SavedViewItem](../../models/savedviewitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
