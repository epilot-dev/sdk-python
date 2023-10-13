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
        'wearily',
    ],
    contexts=[
        shared.WorkflowContext(
            id='<ID>',
            schema='Strontium',
            title='teal 6th Bespoke',
        ),
    ],
    workflow_id='connect',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->