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
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.generate_q_rcode(qrdata='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `qrdata`               | *Optional[str]*        | :heavy_minus_sign:     | Payload of the QR code |


### Response

**[operations.GenerateQRcodeResponse](../../models/operations/generateqrcoderesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_categories

Get all template variable categories

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.variables.get_categories(lang='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `lang`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetCategoriesResponse](../../models/operations/getcategoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_variable_context

Get full variable context

Calls Entity API, User API, Brand API and others to construct full context object used for template variable replace


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetVariableContextRequestBody(
    parameters=shared.VariableParameters(
        brand_id=123451,
        context_data=shared.ContextData(),
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_tags=[
            'string',
        ],
        template_type=shared.TemplateType.EMAIL,
        user_id='50001',
        user_org_id='729224',
        variables_version='2',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## replace_templates

Replace variables in handlebars templates

Takes in an array of input templates and outputs the output text with replaced variables


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ReplaceTemplatesRequestBody(
    inputs=[
        'Hello, {{contact.first_name}}!

        {{{brand.signature}}}
        ',
    ],
    parameters=shared.VariableParameters(
        brand_id=123451,
        context_data=shared.ContextData(),
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_tags=[
            'string',
        ],
        template_type=shared.TemplateType.EMAIL,
        user_id='50001',
        user_org_id='729224',
        variables_version='2',
    ),
)

res = s.variables.replace_templates(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ReplaceTemplatesRequestBody](../../models/operations/replacetemplatesrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ReplaceTemplatesResponse](../../models/operations/replacetemplatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## search_variables

Search variables

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.SearchVariablesRequestBody(
    entity_schemas=[
        'contact',
    ],
    query='logo',
    template_type=shared.TemplateType.DOCUMENT,
)

res = s.variables.search_variables(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.SearchVariablesRequestBody](../../models/operations/searchvariablesrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.SearchVariablesResponse](../../models/operations/searchvariablesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
