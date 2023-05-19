# variables

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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GenerateQRcodeRequest(
    qrdata='enim',
)

res = s.variables.generate_q_rcode(req)

if res.status_code == 200:
    # handle response
```

## get_categories

Get all template variable categories

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetCategoriesRequest(
    lang=operations.GetCategoriesLang.DE,
)

res = s.variables.get_categories(req)

if res.category_results is not None:
    # handle response
```

## get_variable_context

Get full variable context

Calls Entity API, User API, Brand API and others to construct full context object used for template variable replace


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetVariableContextRequestBody(
    parameters=shared.VariableParameters(
        brand_id=123451,
        context_data={
            "quo": 'sequi',
        },
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        language=shared.VariableParametersLanguage.EN,
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_name='id',
        template_tags=[
            'aut',
            'quasi',
            'error',
            'temporibus',
        ],
        template_type=shared.TemplateType.DOCUMENT,
        user_id='50001',
    ),
)

res = s.variables.get_variable_context(req)

if res.variable_context is not None:
    # handle response
```

## replace_templates

Replace variables in handlebars templates

Takes in an array of input templates and outputs the output text with replaced variables


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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
        context_data={
            "voluptatibus": 'vero',
            "nihil": 'praesentium',
            "voluptatibus": 'ipsa',
            "omnis": 'voluptate',
        },
        custom_variables=[
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
            shared.ExternalCustomVariable(
                value='https://partner.epilot.cloud/activate-account?user_name=htny.pct%2Btet%40gmail.com&confirmation_code=EdXPRW19',
                variable='{{craftsmen.invitation_link}}',
            ),
        ],
        language=shared.VariableParametersLanguage.EN,
        main_entity_id='63753437-c9e2-4e83-82bb-b1c666514561',
        template_name='doloremque',
        template_tags=[
            'ut',
            'maiores',
        ],
        template_type=shared.TemplateType.EMAIL,
        user_id='50001',
    ),
)

res = s.variables.replace_templates(req)

if res.replace_templates_200_application_json_object is not None:
    # handle response
```

## search_variables

Search variables

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.SearchVariablesRequestBody(
    entity_schemas=[
        'contact',
        'contact',
    ],
    from_=296140,
    lang=operations.SearchVariablesRequestBodyLang.EN,
    query='logo',
    size=118727,
    template_type=shared.TemplateType.DOCUMENT,
)

res = s.variables.search_variables(req)

if res.variable_results is not None:
    # handle response
```
