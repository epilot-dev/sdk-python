# Variables
(*variables*)

## Overview

Variables

### Available Operations

* [get_categories](#get_categories) - getCategories
* [get_variable_context](#get_variable_context) - getVariableContext
* [replace_templates](#replace_templates) - replaceTemplates
* [search_variables](#search_variables) - searchVariables

## get_categories

Get all template variable categories

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.get_categories()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `lang`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.CategoryResult]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_variable_context

Get full variable context

Calls Entity API, User API, Brand API and others to construct full context object used for template variable replace


### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.get_variable_context(request={
    "parameters": {
        "template_type": epilot_template_variables.TemplateType.EMAIL,
        "brand_id": 123451,
        "custom_variables": [
            {
                "value": "https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19",
                "variable": "{{craftsmen.invitation_link}}",
            },
        ],
        "main_entity_id": "63753437-c9e2-4e83-82bb-b1c666514561",
        "user_id": "50001",
        "user_org_id": "729224",
        "variables_version": "2",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.GetVariableContextRequestBody](../../models/getvariablecontextrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |


### Response

**[models.VariableContext](../../models/variablecontext.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## replace_templates

Replace variables in handlebars templates

Takes in an array of input templates and outputs the output text with replaced variables


### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.replace_templates(request={
    "inputs": [
        "Hello, {{contact.first_name}}!

        {{{brand.signature}}}
        ",
    ],
    "parameters": {
        "template_type": epilot_template_variables.TemplateType.EMAIL,
        "brand_id": 123451,
        "custom_variables": [
            {
                "value": "https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19",
                "variable": "{{craftsmen.invitation_link}}",
            },
        ],
        "main_entity_id": "63753437-c9e2-4e83-82bb-b1c666514561",
        "user_id": "50001",
        "user_org_id": "729224",
        "variables_version": "2",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.ReplaceTemplatesRequestBody](../../models/replacetemplatesrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |


### Response

**[models.ReplaceTemplatesResponseBody](../../models/replacetemplatesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_variables

Search variables

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.search_variables(request={
    "query": "logo",
    "template_type": epilot_template_variables.TemplateType.DOCUMENT,
    "entity_schemas": [
        "contact",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.SearchVariablesRequestBody](../../models/searchvariablesrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |


### Response

**[List[models.VariableResult]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
