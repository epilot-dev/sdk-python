# Variables
(*variables*)

## Overview

Variables

### Available Operations

* [generate_q_rcode](#generate_q_rcode) - generateQRcode
* [get_categories](#get_categories) - getCategories
* [get_variable_context](#get_variable_context) - getVariableContext
* [replace_templates](#replace_templates) - replaceTemplates
* [search_variables](#search_variables) - searchVariables

## generate_q_rcode

Generate QR Code for the given payload

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GenerateQRcodeRequest()

res = s.variables.generate_q_rcode(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GenerateQRcodeRequest](../../models/operations/generateqrcoderequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GenerateQRcodeResponse](../../models/operations/generateqrcoderesponse.md)**


## get_categories

Get all template variable categories

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetCategoriesRequest(
    lang=operations.GetCategoriesLang.DE,
)

res = s.variables.get_categories(req)

if res.category_results is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCategoriesRequest](../../models/operations/getcategoriesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetCategoriesResponse](../../models/operations/getcategoriesresponse.md)**


## get_variable_context

Get full variable context

Calls Entity API, User API, Brand API and others to construct full context object used for template variable replace


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetVariableContextRequestBody(
    parameters=shared.VariableParameters(
        brand_id=123451,
        context_data=shared.VariableParametersContextData(),
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_tags=[
            'Account',
        ],
        template_type=shared.TemplateType.EMAIL,
        user_id='50001',
        user_org_id='729224',
    ),
)

res = s.variables.get_variable_context(req)

if res.variable_context is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetVariableContextRequestBody](../../models/operations/getvariablecontextrequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetVariableContextResponse](../../models/operations/getvariablecontextresponse.md)**


## replace_templates

Replace variables in handlebars templates

Takes in an array of input templates and outputs the output text with replaced variables


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ReplaceTemplatesRequestBody(
    inputs=[
        'H',
        'e',
        'l',
        'l',
        'o',
        ',',
        ' ',
        '{',
        '{',
        'c',
        'o',
        'n',
        't',
        'a',
        'c',
        't',
        '.',
        'f',
        'i',
        'r',
        's',
        't',
        '_',
        'n',
        'a',
        'm',
        'e',
        '}',
        '}',
        '!',
        '
        ',
        '
        ',
        '{',
        '{',
        '{',
        'b',
        'r',
        'a',
        'n',
        'd',
        '.',
        's',
        'i',
        'g',
        'n',
        'a',
        't',
        'u',
        'r',
        'e',
        '}',
        '}',
        '}',
        '
        ',
    ],
    parameters=shared.VariableParameters(
        brand_id=123451,
        context_data=shared.VariableParametersContextData(),
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_tags=[
            'Recycled',
        ],
        template_type=shared.TemplateType.DOCUMENT,
        user_id='50001',
        user_org_id='729224',
    ),
)

res = s.variables.replace_templates(req)

if res.replace_templates_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ReplaceTemplatesRequestBody](../../models/operations/replacetemplatesrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ReplaceTemplatesResponse](../../models/operations/replacetemplatesresponse.md)**


## search_variables

Search variables

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.SearchVariablesRequestBody(
    entity_schemas=[
        'c',
        'o',
        'n',
        't',
        'a',
        'c',
        't',
    ],
    query='logo',
    template_type=shared.TemplateType.DOCUMENT,
)

res = s.variables.search_variables(req)

if res.variable_results is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.SearchVariablesRequestBody](../../models/operations/searchvariablesrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.SearchVariablesResponse](../../models/operations/searchvariablesresponse.md)**

