<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        "provident",
        "distinctio",
        "quibusdam",
    ],
    contexts=[
        shared.WorkflowContext(
            id="nulla",
            schema="corrupti",
            title="Dr.",
        ),
        shared.WorkflowContext(
            id="vel",
            schema="error",
            title="Miss",
        ),
        shared.WorkflowContext(
            id="suscipit",
            schema="iure",
            title="Mrs.",
        ),
    ],
    trigger="AUTOMATIC",
    workflow_id="ipsa",
)
    
res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```
<!-- End SDK Example Usage -->