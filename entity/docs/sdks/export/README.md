# Export
(*export*)

## Overview

Export and Import entities via files

### Available Operations

* [export_entities](#export_entities) - exportEntities

## export_entities

create export file of entities

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.export.export_entities(request={
    "entity_search_params": {
        "q": "_schema:contact AND status:active",
        "aggs": {},
        "fields": [
            "_id",
            "_title",
            "first_name",
            "account",
            "!account.*._files",
            "**._product",
        ],
        "sort": "_created_at:desc",
    },
    "job_id": "abc123",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ExportEntitiesRequest](../../models/exportentitiesrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
