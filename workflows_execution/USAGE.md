<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.WorkflowExecutionCreateReq(
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
    workflow_id='string',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->