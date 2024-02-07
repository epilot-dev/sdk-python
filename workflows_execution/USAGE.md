<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.WorkflowExecutionCreateReq(
    workflow_id='string',
    assigned_to=[
        'string',
    ],
    contexts=[
        shared.WorkflowContext(
            id='<ID>',
            schema='string',
            title='string',
        ),
    ],
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->