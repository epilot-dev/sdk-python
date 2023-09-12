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
        'corrupti',
    ],
    contexts=[
        shared.WorkflowContext(
            id='9bd9d8d6-9a67-44e0-b467-cc8796ed151a',
            schema='perferendis',
            title='Mrs.',
        ),
    ],
    trigger=shared.TriggerType.AUTOMATIC,
    workflow_id='sapiente',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```
<!-- End SDK Example Usage -->