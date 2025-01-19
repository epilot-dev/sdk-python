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
* [patch_saved_view](#patch_saved_view) - patchSavedView
* [update_saved_view](#update_saved_view) - updateSavedView

## create_saved_view

Creates a new saved view

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.create_saved_view(request=epilot_entity.SavedView(
        created_by=epilot_entity.SavedView2(
            **{
                "user_id": "10598",
            },
        ),
        name="View listing German",
        slug=[
            "contact",
        ],
        ui_config={
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

                    ],
                },
            },
        },
        is_favorited_by=[
            "11701",
        ],
        org="66",
        shared_with=[
            "112233",
        ],
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SavedView](../../models/savedview.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateSavedViewResponseBody](../../models/createsavedviewresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_saved_view

Deletes a saved view

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.saved_views.delete_saved_view(request={
        "id": "5ec1756f-b01b-4018-acd1-e0758b2e8f6f",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.DeleteSavedViewRequest](../../models/deletesavedviewrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_saved_view

Gets Saved View configuration by id.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.get_saved_view(request={
        "id": "688c814e-5284-46ef-a5c7-33ab2e585e63",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetSavedViewRequest](../../models/getsavedviewrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSavedViewResponseBody](../../models/getsavedviewresponsebody.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.GetSavedViewSavedViewsResponseBody | 404                                       | application/json                          |
| models.SDKError                           | 4XX, 5XX                                  | \*/\*                                     |

## list_favorite_views_for_user

Get the Favorite Saved Views for user based on the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.list_favorite_views_for_user()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFavoriteViewsForUserResponseBody](../../models/listfavoriteviewsforuserresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_saved_views

Get the Saved Views based on the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.list_saved_views(request={
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

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ListSavedViewsRequest](../../models/listsavedviewsrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListSavedViewsResults](../../models/listsavedviewsresults.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## patch_saved_view

Partially updates a saved view with the provided payload. If an updated_at is passed and the server contains a newer version of the view a `409` error is returned

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.patch_saved_view(request=epilot_entity.PatchSavedViewRequest(
        id="3d9b2e37-06d7-4b73-bca8-367f84b763a6",
        saved_view_partial=epilot_entity.SavedViewPartial(
            created_by=epilot_entity.SavedViewPartial2(
                **{

                },
            ),
            is_favorited_by=[
                "11701",
            ],
            name="View listing German",
            org="66",
            shared_with=[
                "112233",
            ],
            slug=[
                "contact",
            ],
            ui_config={
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

                        ],
                    },
                },
            },
        ),
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.PatchSavedViewRequest](../../models/patchsavedviewrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PatchSavedViewResponseBody](../../models/patchsavedviewresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_saved_view

Updates a saved view

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.saved_views.update_saved_view(request={
        "id": "0002d716-d5b8-417e-be0c-a3f6b7849863",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UpdateSavedViewRequest](../../models/updatesavedviewrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UpdateSavedViewResponseBody](../../models/updatesavedviewresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |